import streamlit as st 
import pickle 
import numpy as np 
with open("./model.pkl", "rb") as f:
    model = pickle.load(f)



feature_1 = st.text_input(
    'alcohol 값을 입력하세요'
)

feature_2 = st.text_input(
    'sugar 값을 입력하세요'
)

feature_3 = st.text_input(
    'pH 값을 입력하세요'
)

button = st.button("제출")

if button:
    test = np.array([float(feature_1), float(feature_2), float(feature_3)]).reshape(-1,3)
    result = model.predict(test)
    if result == 0.0:
        st.write("레드와인")
    else:
        st.write("화이트와인")