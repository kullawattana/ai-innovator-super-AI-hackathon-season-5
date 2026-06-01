import csv

import pandas as pd
df = pd.read_csv('Data.csv')
seldf = df["Temperature"][1:100]
print(seldf)

#MA3 and MA7
ma3 =  []
ma7 = []
for i in range(1,len(seldf)+1):
    print(seldf[i])
    if(i>=3):
        ma3.append(sum(seldf[i-3:i])/3)
    else:
        ma3.append(0)
    if(i>=7):
        ma7.append(sum(seldf[i-7:i])/7)
    else:
        ma7.append(0)

len(seldf)
len(ma3)
len(ma7)

#Plot
import matplotlib.pyplot as mpl
mpl.clf()  #Clear plot
mpl.plot(seldf,'.')
mpl.plot(ma3,color = 'r')
mpl.plot(ma7,color = 'g')
mpl.axis([7,90,20,30])
mpl.show()




