import pandas as pd
import numpy as np
import streamlit as st
import yfinance as yf
import datetime as dt

list = {
    "BTC" : "BTC-USD",
    "ETH" : "ETH-USD",
    "XRP" : "XRP-USD",
    "SHIB" : "SHIB-USD"
}
sec = st.sidebar.selectbox("Cryptocurrency",liste.keys())
ticker = liste.get(sec)

def data(ticker,start="2004-01-01",end=dt.datetime.today().date()):
   df = yf.download(ticker,start,end)
   df=df['Close']
   st.line_chart(df)


col1,col2,col3 = st.columns(3)

with col1:
    last30 = st.button("30 Days")

with col2:
    last90 = st.button("90 Days")

with col3:
    last360 = st.button("365 Days")


today = dt.datetime.today().date()

if last30:
    start = today - dt.timedelta(days=30)
    end = today
elif last90:
    start = today - dt.timedelta(days=90)
    end = today
elif last360:
    start = today - dt.timedelta(days=365)
    end = today
else:
    start = "2004-01-01"
    end = today

veri(ticker,start,end)



