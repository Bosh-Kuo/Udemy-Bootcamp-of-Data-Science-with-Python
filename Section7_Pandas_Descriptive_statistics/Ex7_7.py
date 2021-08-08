import pandas as pd

df = pd.read_csv('./Section7_Pandas_Descriptive_statistics/CardioGoodFitness.csv')
print(df,'\n')
print('covariance matrix:\n', df.cov())
print('\ncorrelation matrix:\n', df.corr())
