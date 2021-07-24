import pandas as pd
 
data = {
    'ABEV3':12.85,
    'AZUL4':22.55,
    'BTOW3':115.08,
    'RENT3':49.03,
    'JBSS3':24.41,
    }
 
serie = pd.Series(data)
print(serie)

serie = serie.append(pd.Series({'PETR4':22.97,'NTCO3':50.6,'TIMP3':14.82}))
print('\n',serie)