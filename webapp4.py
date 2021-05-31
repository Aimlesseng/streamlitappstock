import streamlit as st
from datetime import date
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
from PIL import Image
import time

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.set_page_config(layout="wide")

option = st.sidebar.selectbox('Navigation',('Home','Predict Your Stock','About Us'))

with st.sidebar.beta_expander("Journals and Report"):
	st.write("Research Papers")
	st.write("Final Report")

with st.sidebar.beta_expander("Contact Us"):
	   st.write("Name1 : Contact Num")
	   st.write("Name2 : Contact Num")
	   st.write("Name3 : Contact Num")
	   st.write("Name4 : Contact Num")

with st.sidebar.beta_expander("License"):
	st.write("This webapp is officially licensed to the students of Team 8 of CSE Dept,Marian Engineering College,Tvm")


if option == 'Home' :
    st.title('Stock Forecast App')
    image = Image.open('stck3.jpg')
    st.image(image,width=None)
    st.subheader('Introduction')
    st.write("Trading is tough. Part-time folks trading from their home are up against professionals.The professionals are really great at taking the money.Where there is potential reward, there is potential risk.The results equity curve might only show the reward side of the equation, but risk is always there.So it is a wise idea to implement Artificial intelligence and deep learning technologies into this market which can disrupt the current scenario.In this work we use deep learning architecture and machine learning to predict the future stock prices and further plan to automate intraday trading.")

if option == 'Predict Your Stock' :
    
    selected_stock = st.text_input("Search using stock symbol(For eg ; For Apple,search as AAPL.For Indian stock add '.NS' after stock symbol)", value="AAPL")

    c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12 = st.beta_columns(12)

    with c6:
       st.button("Predict")

    n_years = st.slider('Year of prediction:', 1, 4)
    period = n_years * 365

    @st.cache
    def load_data(ticker):
       data = yf.download(ticker, START, TODAY)
       data.reset_index(inplace=True)
       return data
    
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)
	
    data_load_state = st.text('Loading data...')
    data = load_data(selected_stock)
    data_load_state.text('Loading data... done!')

    st.subheader('Raw data')
    st.write(data.tail())

# Plot raw data
    def plot_raw_data():
	    fig = go.Figure()
	    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	    st.plotly_chart(fig)
	
    plot_raw_data()
    st.write('Forecasting...Please Wait')

# Predict forecast with Prophet.
    df_train = data[['Date','Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

# Show and plot forecast
    st.subheader('Forecast data')
    st.write(forecast.tail())
    
    st.write(f'Forecast plot for {n_years} years')
    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)

    fig2 = m.plot_components(forecast)
    with st.beta_expander("Forecast Components"):
        st.write(fig2)

if option == 'About Us' :
    st.write("This page shows about us")
