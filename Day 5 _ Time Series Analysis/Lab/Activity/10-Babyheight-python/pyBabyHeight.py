age = (18,19,20,21,22,23,24,25,26,27,28,29)
height = (76.1,77,78.1,78.2,78.8,79.7,79.9,81.1,81.2,81.8,82.8,83.5)

#PLOT ORIGINAL DATA
import matplotlib.pyplot as mpl
mpl.clf()  #Clear plot
mpl.plot(age,height,'.')
mpl.show()

#SIMPLE LINEAR REGRESSION
import numpy as np
import statistics as stat
x = np.array(age)
y = np.array(height)
n = len(age)
xy = x*y
xsquare = x**2
sp = sum(xy) - sum(x)*sum(y)/n
ss = sum(xsquare) -  n * stat.mean(x)**2
beta1 = sp/ss
beta0 = stat.mean(y) - beta1 * stat.mean(x)
print(beta0)
print(beta1)


#PREDICTION
childage = 30
childheight = beta0 + beta1 * childage 
print(childheight)