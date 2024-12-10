import pandas
from sklearn import linear_model
df = pandas.read_csv("cardekho_data.csv")
X = df[['Selling_Price', 'Present_Price']]
y = df['Kms_Driven']
regr = linear_model.LinearRegression()
regr.fit(X, y)
predictedKMS = regr.predict([[27000, 55000]])
print(predictedKMS)