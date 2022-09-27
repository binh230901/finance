def stock_price(stock_name):
    import pandas as pd
    from pandas_datareader import data as wb
    price = pd.DataFrame()
    for i in stock_name:
        price[i]= wb.DataReader(i, 'yahoo', start= '2021')['Close']
    return price

def stock_volume(stock):
    import pandas as pd
    from pandas_datareader import data as wb
    stock_volume = pd.DataFrame()
    for i in stock:
        stock_volume[i] = wb.DataReader(i, 'yahoo', start= 2021)['Volume']
    return stock_volume