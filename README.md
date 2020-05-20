# getStooqData
This function downloads selected market data from www.stooq.pl / www.stooq.com as csv files and parse them into a dataframe and return pandas dataframe with OHLC prices and Date as index.

Recquired library - pandas

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
