from locale import currency
from tracemalloc import start
from turtle import onclick
import yfinance as yf
import streamlit as st
import pandas as pd

st.sidebar.write("""# XStocks """)
st.sidebar.write("## WELCOME TO STOCK APP")

name = st.sidebar.text_input("Pleas enter name of stock ","AAPL")




name_stock = name

tickerData = yf.Ticker(name_stock)
Company_name = tickerData.info['shortName']
Company_type = tickerData.info['industry']
pe_ratio = tickerData.info['trailingPE']
country = tickerData.info['country']
avg_vol = tickerData.info['averageVolume']
employees = tickerData.info['fullTimeEmployees']
phone = tickerData.info['phone']
address = tickerData.info['address1']
company_website = tickerData.info['website']
logo_url = tickerData.info['website']
logo_url = "https://logo.clearbit.com/"+ tickerData.info['website']
currency = tickerData.info['currency']
marketprice = tickerData.info['regularMarketPrice']
change  = round(marketprice - tickerData.info['previousClose'] , 2) 
char = "-"
price_percentage  = round((change/tickerData.info['previousClose'])*100,3)

if change >0:
    char = "+ "

st.image(logo_url)
st.write("""# """+ f'{Company_name}')
st.write("## " + f'{marketprice}'+" " + f'{currency}',)
st.write(" ### " + f'{char}' + f' **{change}**' , f'(%{price_percentage})' )
st.write("""### """+ f' {address} , ' +f'{country}')
st.sidebar.write(""" website """ + f' {company_website}')
st.sidebar.write(""" Phone :  """ + f' {phone}')
st.sidebar.write(""" Industry : """ + f' {Company_type}')


starting  = st.sidebar.slider("Starting year", min_value=2000 , max_value=2022 , step=1, value=2022)

ending  = st.sidebar.slider("Ending year", min_value=2000 , max_value=2022 , step=1, value=2022)

tickerDf = tickerData.history(period='id', start=f'{starting}-1-31' , end=f'{ending}-12-31')



st.sidebar.write("""

### Showing *Data* for 
""" + f'{starting}-1-31 to ' + f'{ending}-12-31')



st.write("### Closing")
st.line_chart(tickerDf.Close)
st.write("### Volume")
st.line_chart(tickerDf.Volume)

st.write(""" **PE** :  """ + f' {pe_ratio}' + "     " +"""**Employees** :  """ + f' {employees}')