import pandas as pd
 
data = {
    'ABEV3':12.85,
    'AZUL4':22.55,
    'BTOW3':115.08,
    'RENT3':49.03,
    'JBSS3':24.41,
    }
 
series = pd.Series(data)
list_values = series.tolist()
df = pd.DataFrame(series, columns = ['Prices'])
print(series)
print('\n',list_values)
print('\n',df)

series['RAIL3'] = 18.93
series['JBSS3'] = 21.48
series['SUZB3'] = 48.19
series['MGLU3'] = 25.59
print('\n',series)
