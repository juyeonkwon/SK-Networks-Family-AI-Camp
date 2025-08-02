import chainlit as cl
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.memory import ChatMessageHistory # 세션별 메모리를 위해 사용
from langchain_community.chat_message_histories import RedisChatMessageHistory


memory_store = {}
def get_session_history(session_id: str) -> ChatMessageHistory:
    """세션 ID에 해당하는 대화 기록을 가져오거나 생성"""
    if session_id not in memory_store:
        memory_store[session_id] = ChatMessageHistory()
    return memory_store[session_id]

def get_redis_history(session_id: str) -> RedisChatMessageHistory:
    return RedisChatMessageHistory('encore', url="redis://localhost:6379/0")

@cl.on_chat_start
async def on_chat_start():
    # 모델 초기화
    llm = ChatOpenAI(model="gpt-4.1")

    # 1. 단순화된 프롬프트 (대화 기록 부분이 없음)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "당신은 사용자의 질문에 간결하게 답변하는 AI 비서입니다."),
        MessagesPlaceholder(variable_name='history'),
        ("human", "{input}"),
    ])

    # 2. 단순화된 LCEL 체인
    # 프롬프트, 모델, 출력 파서를 파이프(|)로 연결합니다.
    runnable = prompt | llm 

    chain_with_history = RunnableWithMessageHistory(
            runnable, 
            get_redis_history,
            input_messages_key='input', 
            history_messages_key = 'history'
        )

    # 체인을 사용자 세션에 저장
    cl.user_session.set("chain", chain_with_history)

    await cl.Message(content="안녕하세요! 무엇이든 물어보세요.").send()

@cl.on_message
async def on_message(message: cl.Message):
    # 세션에서 체인 가져오기
    chain = cl.user_session.get("chain")

  
    response = await chain.ainvoke(
        {"input": message.content},
         config={"configurable": {"session_id": cl.user_session.get("encore")}}
        )

    # StrOutputParser 덕분에 response가 바로 문자열이므로 .content 없이 전송
    await cl.Message(content=response.content).send()