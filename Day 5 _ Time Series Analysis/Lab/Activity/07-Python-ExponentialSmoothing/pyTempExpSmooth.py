import pandas as pd
df = pd.read_csv('Data.csv')
seldf = df["Temperature"][0:100]
print(seldf)

#exponential smoothing
es2 =  []
es5 = []
es2.append(25)
es5.append(25)
for i in range(1,len(seldf)):
    r = es2[i-1]+0.2*(seldf[i-1]-es2[i-1])
    es2.append(r)
    r = es5[i-1]+0.5*(seldf[i-1]-es5[i-1])
    es5.append(r)

len(seldf)
len(es2)
len(es5)

#Plot
import matplotlib.pyplot as mpl
mpl.clf()  #Clear plot
mpl.plot(seldf,'.')
mpl.plot(es2,color = 'r')
mpl.plot(es5,color = 'g')
#mpl.axis([7,90,20,30])
mpl.show()




