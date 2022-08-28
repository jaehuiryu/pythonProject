import pandas
from pandas import Series, DataFrame
import ssl

date = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05']
xrp_close = [512, 508, 512, 507, 500]
s = Series(xrp_close, index=date)
print(s)
print(s.index)
print(s.values)

print(s[['2018-08-01', '2018-08-03', '2018-08-05']])

print(s['2018-08-01': '2018-08-03'])

print(s[0 : 5])

print( s / 10)

data2 = {"open": [737, 750], "high": [755, 780], "low": [700, 710], "close": [750, 770]}
df = DataFrame(data2, index=["2018-01-01", "2018-01-02"])
print(df)

df2 = pandas.read_excel("/Users/apple/Documents/test.xlsx")
df2 = df2.set_index('date')
print(df2)

#df2.to_excel("/Users/apple/Documents/test2.xlsx")

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://finance.naver.com/item/sise_day.nhn?code=066570"
df3 = pandas.read_html(url)
print(df3)