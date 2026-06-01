age = (18,19,20,21,22,23,24,25,26,27,28,29)
height = (76.1,77,78.1,78.2,78.8,79.7,79.9,81.1,81.2,81.8,82.8,83.5)

#PLOT ORIGINAL DATA
import matplotlib.pyplot as mpl
mpl.clf()  #Clear plot
mpl.plot(age,height,'.')
mpl.show()

#Method1
import numpy as np
from sklearn import linear_model

X = np.array(age).reshape((-1,1))
y = np.array(height)
model = linear_model.LinearRegression()
model.fit(X,y)
model.predict([[30]])


#Method2
import pandas as pd
import statsmodels.formula.api as smf 

df = pd.DataFrame({'age':age,'height':height}) 
model = smf.ols(formula='height ~ age', 
                data=df).fit() 
  
# model summary 
model.summary()

