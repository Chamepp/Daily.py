import yfinance as yf

# Function to fetch stock market data and analyze it
def analyze_stock(symbol):
    # Fetching stock data
    stock_data = yf.download(symbol)
    
    # Calculating simple moving average (SMA)
    sma = stock_data['Close'].rolling(window=50).mean()
    
    # Calculating exponential moving average (EMA)
    ema = stock_data['Close'].ewm(span=20, adjust=False).mean()
    
    # Printing analysis results
    print("Stock Symbol:", symbol)
    print("Stock Data:")
    print(stock_data)
    print("Simple Moving Average (SMA):")
    print(sma)
    print("Exponential Moving Average (EMA):")
    print(ema)

# Example usage
analyze_stock('AAPL')  # Replace 'AAPL' with the desired stock symbol
