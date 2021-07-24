import pandas as pd

products = {
    'product1': {2008:7, 2009:9, 2010: 10, 2011: 15, 2012: 50, 2013: 47}, 
    'product2': {2008:14, 2009:13, 2010: 7, 2011: 13, 2012: 77, 2013: 94}, 
    'product3': {2008:5, 2009:11, 2010: 3, 2011: 45, 2012: 21, 2013: 33},
    'product4': {2008:4, 2009:2, 2010: 3, 2011: 45, 2012: 21, 2013: 33}}
df = pd.DataFrame(products)
df.columns.name='products'
df.index.name='Year'
print(df)