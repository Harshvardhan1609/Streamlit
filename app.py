import streamlit as st
import yfinance as yf

st.sidebar.title("StocK APP")
st.audio('net.mp3', start_time=0)
st.sidebar.header("Introduction")
st.sidebar.write("It is an simple stock app in which we will see the market data in a nutshell")

ticker = 'AAPL'

ticker = st.text_input("Enter the ticker Name")

tickerData = yf.Ticker(ticker)

st.sidebar.write("It is an sidebar")
a = st.sidebar.slider("tick",1,10)
st.write(a)

st.sidebar.subheader("Company Details")
st.sidebar.write(tickerData.info['longBusinessSummary'])
st.sidebar.write("City of Operation")
st.sidebar.write(tickerData.info['city'])
st.sidebar.write("Country")
st.sidebar.write(tickerData.info['country'])
st.write(tickerData.info['sectorKey'])
a = "https://logo.clearbit.com/"
company_name = tickerData.info['website']
final = a+company_name

tickerDataFrame  = tickerData.history(period='1d',start='2010-5-31',end='2020-5-31')

st.image(final)
st.video('https://www.youtube.com/watch?v=2qAQSQgYnS4')

st.line_chart(tickerDataFrame.Close)
st.line_chart(tickerDataFrame.Volume)