# Quantitative-Analysis-of-Price-Daily-Returns
### Aim at answering 3 questions to the stock price and the daily returns:
- Can returns be described with a normal distribution?
- Is directional bias in daily change?
- Can price movement be described as a random walk?

### to find can returns be described with a normal distribution?
- using the mean, std, and number of datas of amzn_return to create a normal dist, then compare it with the real distribution by plotting histogram of stock price change with normal curve overlay
- apply hypothesis testing to test whether the sample drawn from a population is under normal dist
- the null hypo assumes the sample is under normal distribution
- for t-test scores, generally we need t test to be over +-2 to start rejecting
- A p-value less than 0.05 is statistically significant. It indicates strong evidence against the null hypothesis, as there is less than a 5% probability we will commit type 1 error that we reject the null while we should not. Therefore, we reject the null hypothesis, and accept the alternative hypothesis that the sample is not under normal dist

### to find is directional bias in daily change?
- A skewness value greater than 1 or less than -1 indicates a highly skewed distribution. A value between 0.5 and 1 or -0.5 and -1 is moderately skewed. A value between -0.5 and 0.5 indicates that the distribution is fairly symmetrical
- Conduct simple hypothesis test, in short, we assume population has no directional bias of return, and try to use the sample we have to support or reject it
- so use t-test, setting expected population mean as 0

### to find can price movement be described as a random walk?
- if the price change is random, the best predictor is using today's price to predict tomorrow's price, should have no pattern we can find
- create price lag as independent variables to explain the price change and apply linear least square method to conduct the regression to get the coefficient of x1 and x2 (the lag1 and lag2, as independent variables in this case)
- then use the findings to make prediction and compare with the sample
- visualize the difference graphically, also find the standard error by calculating the Root Mean Square Error of the regression model
