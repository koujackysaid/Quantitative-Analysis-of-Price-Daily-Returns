import numpy as np
import pandas as pd
import pandas_datareader as reader
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['figure.figsize']=8,6
import seaborn as sb
sb.set()
from scipy import stats

# 1
stock = 'AAPL'
aapl = reader.get_data_yahoo(stock)['Adj Close']
aapl_return = round(np.log(aapl).diff().dropna()*100, 2) # as%
aapl_return[-252:].plot()
plt.title('aapl_daily log return_value in %')
plt.show()

#2
aapl_return.describe()
n, minmax, mean, var, skew, kurt = stats.describe(aapl_return)
mini, maxi =  minmax
std = var**(1/2)

#3
plt.hist(aapl_return, bins=15)
plt.title('aapl daily log return distribution')
plt.show()
x = stats.norm.rvs(mean, std, n)
plt.hist(x, bins=15)
plt.title('normal distribution')
plt.show()

#4
x_test = stats.kurtosistest(x)
aapl_test = stats.kurtosistest(aapl_return)
print('kurtosis test assume sample drawn from population under norm dist with Kurt=3\n')
print(f'{"     Test statistic":20}{"p-value":>15}')
print(f'{" "*5}{"-"* 30}')
print(f"x:{x_test[0]:>17.2f}{x_test[1]:16.4f}")
print(f"AAPL: {aapl_test[0]:13.2f}{aapl_test[1]:16.4f}\n")

#5
plt.hist(aapl_return, bins=25, edgecolor='black',density=True)
overlay = np.linspace(mini, maxi, 100)
plt.plot(overlay, stats.norm.pdf(overlay, mean, std))
plt.title('aapl return with normal distribution overlay')
plt.show()
# if want zoom in
# plt.xlim(-5,5)
plt.hist(x, bins=25, density=True)
b = np.linspace(mini, maxi, 100)
plt.plot(b, stats.norm.pdf(b, mean, std))
plt.title('sample with norm_ dist with normal distribution overlay')
plt.show()

#6
tstat, pvalue =  np.round(stats.ttest_1samp(aapl_return, 0, alternative='two-sided'),2)
print('t-test, null setting sample drawn from population with mean = 0, no directional bias\n')
print('tstat= ', tstat,'p-value = ', pvalue,'\n')
# if want to pick a sample from the sample we have
# tstat, pvalue =  np.round(stats.ttest_1samp(aapl_return.sample(252), 0, alternative='two-sided'),2)

#7
aapl = pd.DataFrame(aapl)
aapl['lag1'] = aapl['Adj Close'].shift(1) # need to state clear which col to shift, cant be aapl directly
aapl['lag2'] = aapl['Adj Close'].shift(2)
aapl.dropna(inplace=True)

lr = np.linalg.lstsq(aapl[['lag1','lag2']], aapl['Adj Close'], rcond=False)[0]
print('lr: ', lr, '\n')

aapl['predict'] = np.dot(aapl[['lag1','lag2']],lr)
aapl['error'] = aapl['predict'] - aapl['Adj Close']
SSE = aapl['error'].sum()
SSE = np.abs(SSE)
df = 2
MSE = SSE/df
RMSE = MSE**(1/2)
print('RMSE(standard error of the sample): ', RMSE,'\n')

aapl[['predict', 'Adj Close']].iloc[-252:].plot()
plt.title('prediction vs observed sample')
plt.show()

plt.hist(aapl['error'], bins=30)
plt.title('frequency of prediction error by simple OLS linear regression')

print('DF:\n')
print(aapl.head())



