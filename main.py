import streamlit as st
import datetime as dt
import yfinance as yf

st.title("EDIT 2000E Unit 4 Project | Ben Nodvin")

st.text("Get Recent Stock Data:")

ticker = st.text_input("Ticker","AAPL")

start = st.date_input("Start date:",dt.datetime.now() - dt.timedelta(days=365))
end = st.date_input("End date:",dt.datetime.now())

data = yf.download(ticker,start,end)

if data.empty:
    st.error("Invalid Ticker")
else:
    data
    st.balloons()

avg_rate_of_change = data["Adj Close"].pct_change(12).mean()
st.text("Average Rate of Change YoY")
st.text(str(avg_rate_of_change*100)+"%")

all_time_high = data["Adj Close"].max()
st.text("All Time High")
st.text("$"+str(all_time_high))

all_time_low = data["Adj Close"].min()
st.text("All Time Low")
st.text("$"+str(all_time_low))


st.subheader("Adjusted Close Line Chart")
st.line_chart(data["Adj Close"])




