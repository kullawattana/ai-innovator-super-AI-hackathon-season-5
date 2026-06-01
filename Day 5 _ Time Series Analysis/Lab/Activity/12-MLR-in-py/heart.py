import pandas as pd
df = pd.read_csv('Heart.csv')

print(df.columns)


#Plot
import matplotlib.pyplot as mpl
mpl.clf()  #Clear plot
mpl.plot(df['Age'],'.')
mpl.plot(df['MaxHR'],color = 'r')
#mpl.axis([7,90,20,30])
mpl.show()




