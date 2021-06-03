from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components
from datetime import date
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
from PIL import Image
import time
import base64
import webbrowser
from bokeh.models.widgets import Div


START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.set_page_config(layout="wide")

option = st.sidebar.selectbox('Navigation',('Home','Predict Your Stock','About Us'))


with st.sidebar.beta_expander("Contact Us"):
	   st.write("sam3tech@gmail.com")
	   st.write("sidharthsnl83@gmail.com")
	   st.write("vishnujk95@gmail.com")
	   st.write("buddhaprabodh224@gmail.com")

with st.sidebar.beta_expander("License"):
	st.write("This webapp is officially licensed to the students of Team 8 of CSE Dept,Marian Engineering College,Tvm")


if option == 'Home' :
    components.html(
    """
 <!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="Sambhu Sidharth Vishnu Budha">
  <link rel="icon" href="/docs/4.0/assets/img/favicons/favicon.ico">

  <title>Stock forecast</title>

  <link rel="canonical" href="https://getbootstrap.com/docs/4.0/examples/blog/">

  <!-- Bootstrap core CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  <link href="../../dist/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom styles for this template -->
  <link href="https://fonts.googleapis.com/css?family=Playfair+Display:700,900" rel="stylesheet">
  <link href="blog.css" rel="stylesheet">
  <style media="screen">
    /* cyrillic */
    @font-face {
      font-family: 'Playfair Display';
      font-style: normal;
      font-weight: 700;
      src: url(https://fonts.gstatic.com/s/playfairdisplay/v22/nuFiD-vYSZviVYUb_rj3ij__anPXDTjYgFE_.woff2) format('woff2');
      unicode-range: U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116;
    }

    /* vietnamese */
    @font-face {
      font-family: 'Playfair Display';
      font-style: normal;
      font-weight: 700;
      src: url(https://fonts.gstatic.com/s/playfairdisplay/v22/nuFiD-vYSZviVYUb_rj3ij__anPXDTPYgFE_.woff2) format('woff2');
      unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;
    }

    /* latin-ext */
    @font-face {
      font-family: 'Playfair Display';
      font-style: normal;
      font-weight: 700;
      src: url(https://fonts.gstatic.com/s/playfairdisplay/v22/nuFiD-vYSZviVYUb_rj3ij__anPXDTLYgFE_.woff2) format('woff2');
      unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
    }

    /* latin */
    @font-face {
      font-family: 'Playfair Display';
      font-style: normal;
      font-weight: 700;
      src: url(https://fonts.gstatic.com/s/playfairdisplay/v22/nuFiD-vYSZviVYUb_rj3ij__anPXDTzYgA.woff2) format('woff2');
      unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
    }

    /* cyrillic */
    @font-face {
      font-family: 'Playfair Display';
      font-style: normal;
      font-weight: 900;
      src: url(https://fonts.gstatic.com/s/playfairdisplay/v22/nuFiD-vYSZviVYUb_rj3ij__anPXDTjYgFE_.woff2) format('woff2');
      unicode-range: U+0400-045F, U+0490-0491, U+04B0-04B1, U+2116;
    }

    /* vietnamese */
    @font-face {
      font-family: 'Playfair Display';
      font-style: normal;
      font-weight: 900;
      src: url(https://fonts.gstatic.com/s/playfairdisplay/v22/nuFiD-vYSZviVYUb_rj3ij__anPXDTPYgFE_.woff2) format('woff2');
      unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB;
    }

    /* latin-ext */
    @font-face {
      font-family: 'Playfair Display';
      font-style: normal;
      font-weight: 900;
      src: url(https://fonts.gstatic.com/s/playfairdisplay/v22/nuFiD-vYSZviVYUb_rj3ij__anPXDTLYgFE_.woff2) format('woff2');
      unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
    }

    /* latin */
    @font-face {
      font-family: 'Playfair Display';
      font-style: normal;
      font-weight: 900;
      src: url(https://fonts.gstatic.com/s/playfairdisplay/v22/nuFiD-vYSZviVYUb_rj3ij__anPXDTzYgA.woff2) format('woff2');
      unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
    }

    /* stylelint-disable selector-list-comma-newline-after */

    .blog-header {
      line-height: 1;
      border-bottom: 1px solid #e5e5e5;
    }

    .blog-header-logo {
      font-family: "Playfair Display", Georgia, "Times New Roman", serif;
      font-size: 2.25rem;
    }

    .blog-header-logo:hover {
      text-decoration: none;
    }

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
      font-family: "Playfair Display", Georgia, "Times New Roman", serif;
    }

    .display-4 {
      font-size: 2.5rem;
    }

    @media (min-width: 768px) {
      .display-4 {
        font-size: 3rem;
      }
    }

    .nav-scroller {
      position: relative;
      z-index: 2;
      height: 2.75rem;
      overflow-y: hidden;
    }

    .nav-scroller .nav {
      display: -webkit-box;
      display: -ms-flexbox;
      display: flex;
      -ms-flex-wrap: nowrap;
      flex-wrap: nowrap;
      padding-bottom: 1rem;
      margin-top: -1px;
      overflow-x: auto;
      text-align: center;
      white-space: nowrap;
      -webkit-overflow-scrolling: touch;
    }

    .nav-scroller .nav-link {
      padding-top: .75rem;
      padding-bottom: .75rem;
      font-size: .875rem;
    }

    .card-img-right {
      height: 100%;
      border-radius: 0 3px 3px 0;
    }

    .flex-auto {
      -ms-flex: 0 0 auto;
      -webkit-box-flex: 0;
      flex: 0 0 auto;
    }

    .h-250 {
      height: 250px;
    }

    @media (min-width: 768px) {
      .h-md-250 {
        height: 250px;
      }
    }

    .border-top {
      border-top: 1px solid #e5e5e5;
    }

    .border-bottom {
      border-bottom: 1px solid #e5e5e5;
    }

    .box-shadow {
      box-shadow: 0 .25rem .75rem rgba(0, 0, 0, .05);
    }

    /*
 * Blog name and description
 */
    .blog-title {
      margin-bottom: 0;
      font-size: 2rem;
      font-weight: 400;
    }

    .blog-description {
      font-size: 1.1rem;
      color: #999;
    }

    @media (min-width: 40em) {
      .blog-title {
        font-size: 3.5rem;
      }
    }

    /* Pagination */
    .blog-pagination {
      margin-bottom: 4rem;
    }

    .blog-pagination>.btn {
      border-radius: 2rem;
    }

    /*
 * Blog posts
 */
    .blog-post {
      margin-bottom: 4rem;
    }

    .blog-post-title {
      margin-bottom: .25rem;
      font-size: 2.5rem;
    }

    .blog-post-meta {
      margin-bottom: 1.25rem;
      color: #999;
    }

    /*
 * Footer
 */
    .blog-footer {
      padding: 2.5rem 0;
      color: #999;
      text-align: center;
      background-color: #f9f9f9;
      border-top: .05rem solid #e5e5e5;
    }

    .blog-footer p:last-child {
      margin-bottom: 0;
    }
  </style>


</head>

<body>

  <div class="container">
    <header class="blog-header py-3">
      <div class="row flex-nowrap justify-content-between align-items-center">
        <div class="col-4 pt-1">
          <a class="text-muted" href="#"></a>
        </div>
        <div class="col-4 text-center">
          <a class="blog-header-logo text-dark" href="#">STOCK FORECASTER</a>
        </div>
        <div class="col-4 d-flex justify-content-end align-items-center">
          <a class="text-muted" href="#">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mx-3">
              <circle cx="10.5" cy="10.5" r="7.5"></circle>
              <line x1="21" y1="21" x2="15.8" y2="15.8"></line>
            </svg>
          </a>
          <a class="" href="#"></a>
        </div>
      </div>
    </header>



    <div class="jumbotron p-3 p-md-5 text-white rounded bg-dark">
      <div class="col-md-6 px-0">
        <h1 class="display-4 font-italic">Predict your Stocks!!!</h1>
        <p class="lead my-3">Learn more about the market and be a great trader by using our machine learning tools to predict the future stock prices</p>
        <!-- <p class="lead mb-0"><a href="#" class="text-white font-weight-bold">Continue reading...</a></p> -->
      </div>
    </div>


  </div>
  </div>

  <main role="main" class="container">
    <div class="row">
      <div class="col-md-8 blog-main">
        <h3 class="pb-3 mb-4 font-italic border-bottom">
          WELOCOME TO THE WORLD OF TRADING
        </h3>

        <div class="blog-post">
          <h2 class="blog-post-title">Stock Market</h2>


          <p>It is a place where shares of pubic listed companies are traded. A stock exchange facilitates stock brokers to trade company stocks and other securities. ... A stock may be bought or sold only if it is listed on an exchange.</p>
          <hr>
          <p>The stock market refers to the collection of markets and exchanges where regular activities of buying, selling, and issuance of shares of publicly-held companies take place. Such financial activities are conducted through
            institutionalized formal exchanges or over-the-counter (OTC) marketplaces which operate under a defined set of regulations. There can be multiple stock trading venues in a country or a region which allow transactions in stocks and other
            forms of securities..</p>
          <blockquote>
            <p>While both terms - stock market and stock exchange - are used interchangeably, the latter term is generally a subset of the former. If one says that she trades in the stock market, it means that she buys and sells shares/equities on
              one (or more) of the stock exchange(s) that are part of the overall stock market. The leading stock exchanges in the U.S. include the New York Stock Exchange (NYSE), Nasdaq, and the Chicago Board Options Exchange (CBOE). These leading
              national exchanges, along with several other exchanges operating in the country, form the stock market of the U.S.</p>
          </blockquote>
          <p>Though it is called a stock market or equity market and is primarily known for trading stocks/equities, other financial securities - like exchange traded funds (ETF), corporate bonds and derivatives based on stocks, commodities,
            currencies, and bonds - are also traded in the stock markets.</p>
          <h2>Understanding the Stock Market</h2>
          <p>While today it is possible to purchase almost everything online, there is usually a designated market for every commodity. For instance, people drive to city outskirts and farmlands to purchase Christmas trees, visit the local timber
            market to buy wood and other necessary material for home furniture and renovations, and go to stores like Walmart for their regular grocery supplies.<br>
            Such dedicated markets serve as a platform where numerous buyers and sellers meet, interact and transact. Since the number of market participants is huge, one is assured of a fair price. For example, if there is only one seller of
            Christmas trees in the entire city, he will have the liberty to charge any price he pleases as the buyers won’t have anywhere else to go. If the number of tree sellers is large in a common marketplace, they will have to compete against
            each other to attract buyers. The buyers will be spoiled for choice with low- or optimum-pricing making it a fair market with price transparency. Even while shopping online, buyers compare prices offered by different sellers on the same
            shopping portal or across different portals to get the best deals, forcing the various online sellers to offer the best price.<br>
            A stock market is a similar designated market for trading various kinds of securities in a controlled, secure and managed environment. Since the stock market brings together hundreds of thousands of market participants who wish to buy and
            sell shares, it ensures fair pricing practices and transparency in transactions. While earlier stock markets used to issue and deal in paper-based physical share certificates, the modern day computer-aided stock markets operate
            electronically. </p>

          <h3>How the Stock Market Works</h3>
          <p>In a nutshell, stock markets provide a secure and regulated environment where market participants can transact in shares and other eligible financial instruments with confidence with zero- to low-operational risk. Operating under the
            defined rules as stated by the regulator, the stock markets act as primary markets and as secondary markets.<br>
            As a primary market, the stock market allows companies to issue and sell their shares to the common public for the first time through the process of initial public offerings (IPO). This activity helps companies raise necessary capital
            from investors. It essentially means that a company divides itself into a number of shares (say, 20 million shares) and sells a part of those shares (say, 5 million shares) to common public at a price (say, $10 per share).<br>
            To facilitate this process, a company needs a marketplace where these shares can be sold. This marketplace is provided by the stock market. If everything goes as per the plans, the company will successfully sell the 5 million shares at a
            price of $10 per share and collect $50 million worth of funds. Investors will get the company shares which they can expect to hold for their preferred duration, in anticipation of rising in share price and any potential income in the form
            of dividend payments. The stock exchange acts as a facilitator for this capital raising process and receives a fee for its services from the company and its financial partners.<br>
            Following the first-time share issuance IPO exercise called the listing process, the stock exchange also serves as the trading platform that facilitates regular buying and selling of the listed shares. This constitutes the secondary
            market. The stock exchange earns a fee for every trade that occurs on its platform during the secondary market activity.<br>
            The stock exchange shoulders the responsibility of ensuring price transparency, liquidity, price discovery and fair dealings in such trading activities. As almost all major stock markets across the globe now operate electronically, the
            exchange maintains trading systems that efficiently manage the buy and sell orders from various market participants. They perform the price matching function to facilitate trade execution at a price fair to both buyers and sellers.<br>
            A listed company may also offer new, additional shares through other offerings at a later stage, like through rights issue or through follow-on offers. They may even buyback or delist their shares. The stock exchange facilitates such
            transactions.<br>
            The stock exchange often creates and maintains various market-level and sector-specific indicators, like the S&P 500 index or Nasdaq 100 index, which provide a measure to track the movement of the overall market. Other methods include the
            Stochastic Oscillator and Stochastic Momentum Index.<br>
            The stock exchanges also maintain all company news, announcements, and financial reporting, which can be usually accessed on their official websites. A stock exchange also supports various other corporate-level, transaction-related
            activities. For instance, profitable companies may reward investors by paying dividends which usually comes from a part of the company’s earnings. The exchange maintains all such information and may support its processing to a certain
            extent. </p>




        </div><!-- /.blog-post -->






      </div><!-- /.blog-main -->

      <aside class="col-md-4 blog-sidebar">
        <div class="p-3 mb-3 bg-light rounded">
          <h4 class="font-italic">Disclaimer</h4>
          <p class="mb-0">Mutual Fund investments are subject to market risks, read all scheme related documents carefully. The NAVs of the schemes may go up or down depending upon the factors and forces affecting the securities market including the
            fluctuations in the interest rates. The past performance of the mutual funds is not necessarily indicative of future performance of the schemes. The Mutual Fund is not guaranteeing or assuring any dividend under any of the schemes and the
            same is subject to the availability and adequacy of distributable surplus. Investors are requested to review the prospectus carefully and obtain expert professional advice with regard to specific legal, tax and financial implications of
            the investment/participation in the scheme.

            While all efforts have been taken to make this web site as authentic as possible, please refer to the print versions, notified Gazette copies of Acts/Rules/Regulations for authentic version or for use before any authority. We will not be
            responsible for any loss to any person/entity caused by any short-coming, defect or inaccuracy inadvertently or otherwise crept in the Mutual Funds Sahi Hai web site.</p>
        </div>

        <div class="p-3">
          <h4 class="font-italic">Term Library</h4>
          <ol class="list-unstyled mb-0">
            <li>Bear Market</li>
            <li>Blue Chip Stoc</li>
            <li>Board Lot</li>
            <li>Bonds</li>
            <li>Bull Market</li>
            <li>Call Option</li>
            <li>Close Price</li>
            <li>Debentures</li>
            <li>Delta</li>
            <li>Face value</li>

          </ol>
        </div>


      </aside><!-- /.blog-sidebar -->

    </div><!-- /.row -->

  </main><!-- /.container -->

  <footer class="blog-footer">
    <p>Officially licensed to the students of Team 8 of CSE Dept,Marian Engineering College,Tvm</p>
    <p>
      2021
    </p>
  </footer>

  <!-- Bootstrap core JavaScript
    ================================================== -->
  <!-- Placed at the end of the document so the pages load faster -->
  <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
  <script>
    window.jQuery || document.write('<script src="../../assets/js/vendor/jquery-slim.min.js"><\/script>')
  </script>
  <script src="../../assets/js/vendor/popper.min.js"></script>
  <script src="../../dist/js/bootstrap.min.js"></script>
  <script src="../../assets/js/vendor/holder.min.js"></script>
  <script>
    Holder.addTheme('thumb', {
      bg: '#55595c',
      fg: '#eceeef',
      text: 'Thumbnail'
    }); <
    script src = "https://code.jquery.com/jquery-3.2.1.slim.min.js"
    integrity = "sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
    crossorigin = "anonymous" >
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </script>
</body>

</html>


    """,
    height=4800,
    )

    # st.title('Stock Forecast App')
    # # image = Image.open('/Users/Sidharth S/Desktop/stck2.jpg')
    # #st.image(image,width=None)
    # st.subheader('Introduction')
    # st.write("Trading is tough. Part-time folks trading from their home are up against professionals.The professionals are really great at taking the money.Where there is potential reward, there is potential risk.The results equity curve might only show the reward side of the equation, but risk is always there.So it is a wise idea to implement Artificial intelligence and deep learning technologies into this market which can disrupt the current scenario.In this work we use deep learning architecture and machine learning to predict the future stock prices and further plan to automate intraday trading.")

if option == 'Predict Your Stock' :
    st.title('PREDICT YOUR FAVORITE STOCKS HERE')
    
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
    
    
    components.html(
    """
    <!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="Aimless">
  <link rel="icon" href="/docs/4.0/assets/img/favicons/favicon.ico">

  <title>About Us</title>

  <link rel="canonical" href="https://getbootstrap.com/docs/4.0/examples/album/">
  <!-- Bootstrap core CSS -->
  <<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <!-- Custom styles for this template -->
    <link href="album.css" rel="stylesheet">
    <style media="screen">
      :root {
        --jumbotron-padding-y: 3rem;
      }

      .jumbotron {
        padding-top: var(--jumbotron-padding-y);
        padding-bottom: var(--jumbotron-padding-y);
        margin-bottom: 0;
        background-color: #fff;
      }

      @media (min-width: 768px) {
        .jumbotron {
          padding-top: calc(var(--jumbotron-padding-y) * 2);
          padding-bottom: calc(var(--jumbotron-padding-y) * 2);
        }
      }

      .jumbotron p:last-child {
        margin-bottom: 0;
      }

      .jumbotron-heading {
        font-weight: 300;
      }

      .jumbotron .container {
        max-width: 40rem;
      }

      footer {
        padding-top: 3rem;
        padding-bottom: 3rem;
      }

      footer p {
        margin-bottom: .25rem;
      }

      .box-shadow {
        box-shadow: 0 .25rem .75rem rgba(0, 0, 0, .05);
      }
    </style>
</head>

<body>



  <main role="main">

    <section class="jumbotron text-center">
      <div class="container">
        <h1 class="jumbotron-heading">STOCK FORECASTING AND ANALYSIS USING LSTM AND PROPHET
        </h1>
        <p class="lead text-muted">Here we provide a web platform where you can predict the future stock prices of different companies using machine learning algorithms namely LSTM and Prophet. Performance analysis is performed inorder to find the
          better model</p>
        
      </div>
    </section>


    </div>

  </main>

  

  <!-- Bootstrap core JavaScript
    ================================================== -->
  <!-- Placed at the end of the document so the pages load faster -->
  <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
  <script>
    window.jQuery || document.write('<script src="../../assets/js/vendor/jquery-slim.min.js"><\/script>')
  </script>
  <script src="../../assets/js/vendor/popper.min.js"></script>
  <script src="../../dist/js/bootstrap.min.js"></script>
  <script src="../../assets/js/vendor/holder.min.js"></script>
</body>

</html>
""",
    height=400,
    )

    c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12 = st.beta_columns((1,1,1,1,1,1,2,1,1,1,1,1))
    giturl = 'https://github.com/Aimlesseng/streamlitappstock'
    paperurl = 'https://drive.google.com/drive/folders/1aF9UOtgymjedGmiEkUqXNdNnyp3bACN1'

    with c6:
       if st.button('Github'):
          js = "window.open('https://github.com/Aimlesseng/streamlitappstock')"  # New tab or window
          html = '<img src onerror="{}">'.format(js)
          div = Div(text=html)
          st.bokeh_chart(div)
    
    with c7:
      if st.button('Paper Works'):
          js = "window.open('https://drive.google.com/drive/folders/1aF9UOtgymjedGmiEkUqXNdNnyp3bACN1')"  # New tab or window
          html = '<img src onerror="{}">'.format(js)
          div = Div(text=html)
          st.bokeh_chart(div)
    
    
    
    def img_to_bytes(img_path):
        img_bytes = Path(img_path).read_bytes()
        encoded = base64.b64encode(img_bytes).decode()
        return encoded

    c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12= st.beta_columns(12)
    m1,m2,m3,m4,m5,m6= st.beta_columns(6)
    with c2:
        header_html = "<img src='data:image/png;base64,{}' class='img-fluid' height='250' width='250'>".format(img_to_bytes("sam.jpg"))
        st.markdown(header_html, unsafe_allow_html=True,)

    with c8:
        header_html = "<img src='data:image/png;base64,{}' class='img-fluid' height='250' width='250'>".format(img_to_bytes("sid.jpg"))
        st.markdown(header_html, unsafe_allow_html=True,)
    
    with m2:
        st.write("  __Sambhu S S__  \n__Roll No:26__")

    with m5:
        st.write("  __Sidharth S__  \n__Roll No:28__")

    k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12= st.beta_columns(12)
    l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12= st.beta_columns((1,1,3,1,1,1,1,1,3,1,1,1))

    with k2:
        header_html = "<img src='data:image/png;base64,{}' class='img-fluid' height='250' width='250'>".format(img_to_bytes("potts.jpg"))
        st.markdown(header_html, unsafe_allow_html=True,)

    with k8:
        header_html = "<img src='data:image/png;base64,{}' class='img-fluid' height='250' width='250'>".format(img_to_bytes("bud.jpg"))
        st.markdown(header_html, unsafe_allow_html=True,)
    
    with l3:
        st.write("  __Vishnu Jayakumar__  \n  __Roll No:32__")

    with l9:
        st.write("  __Buddha Prabodh J S__  \n  __Roll No:10__")
    
    
        
