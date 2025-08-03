import streamlit as st 
import pandas as pd 
import pymysql


conn = pymysql.connect(host='127.0.0.1', user='', passwd='', database='', port=3306)
cur = conn.cursor()

def get_sql(sql):
    cur.execute(sql)
    return cur.fetchall()

input_sql = st.text_input(label='SQL 입력력')

if input_sql:
    try:
        rt = get_sql(input_sql)
        st.write(pd.DataFrame(rt))
    except Exception as e : 
        st.write(e)

    
