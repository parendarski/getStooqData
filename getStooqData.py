import pandas as pd

def getStooqData(symbol, start, end, freq):

#     """Download selected market data from www.stooq.pl as csv files and parse them into a dataframe and
#     return pandas dataframe with OHLC prices and Date as index.

#     Parameters
#     ----------
#     symbol : string
#         Selected symbol
#     start : string 
#         Start date, format yyyymmdd
#     end : string
#         End date, format yyyymmdd
#     freq : string
#         period: d, w, m, y
#
#     Returns
#     -------
#     dataframe : pandas dataframe
#         Return pandas dataframe with OHLC prices and Date as index.
#     
#     Examples
#     -------
#     getStooqData('MSFT.US', '20190120', '20190520', 'd') # use daily data
#     getStooqData('BTC.V', '20190120', '20190520', 'y') # use yearly data
#     getStooqData('EURDKK', '20190120', '20190520', 'w') # use weekly data
#  
#     """

    url = f'https://stooq.com/q/d/l/?s={symbol}&d1={start}&d2={end}&i={freq}'
    df = pd.read_csv(url, index_col='Date')  
    return df