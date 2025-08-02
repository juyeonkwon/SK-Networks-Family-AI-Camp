from datetime import date, datetime
import requests 
import pandas as pd 
import io
def get_exchage(exchange='USD', date_=None, type_='buy'):
    """  
        exchange는 환율 코드 입력 -> 예) USD
        date_ -> 날짜 형식 20250525
        type_ -> buy, sell
    """
    global exchange_df
    try:
        datetime.strptime(date_, '%Y%m%d')
    except:
        print("날짜 형식을 지켜주세요")
        return
    hana = "https://www.kebhana.com/cms/rate/wpfxd651_01i_01.do"
    payload ={"ajax" : "true",
                "curCd" : "",
                "pbldDvCd" : "0",
                "pbldSqn" : "",
                "hid_key_data" : "",
                "inqKindCd" : "1",
                "hid_enc_data" : "",
                "requestTarget" : "searchContentDiv",}
    payload['inqStrDt'] = date_.replace("-", "")
    exchange_df = pd.read_html(io.StringIO(requests.post(hana, data=payload).text))[0]
    exchange_df.columns = ["_".join(sorted(list(set([x,y,z])))) for x, y, z in exchange_df.columns]
    return exchange_df.loc[exchange_df['통화'].str.find(exchange.upper()) > -1, '사실 때_현찰_환율' if type_ == "buy" else '파실 때_현찰_환율' ].values[0]