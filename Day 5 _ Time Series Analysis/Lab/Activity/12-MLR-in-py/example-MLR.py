x1 = (11,22,33,44,55)
x2 = (1.1,1.2,1.3,1.5,1.9)
y = (22,33,44,55,55)

#Method1
import numpy as np
import pandas as pd
from sklearn import linear_model

df = pd.DataFrame({'x1':x1,'x2':x2,'y':y})
X = df[['x1','x2']]
y = df['y']
model = linear_model.LinearRegression()
model.fit(X,y)
model.predict([[11,2]])


#Method2
import statsmodels.formula.api as smf 
model = smf.ols(formula='y ~ x1+x2',data=df).fit() 
  
# model summary 
model.summary()

