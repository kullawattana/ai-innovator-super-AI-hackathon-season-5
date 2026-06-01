import pandas as pd
df = pd.read_csv('Data.csv')
seldf = df["Temperature"][0:30*24]
print(seldf)

#PLOT ORIGINAL DATA
import matplotlib.pyplot as mpl
mpl.clf()  #Clear plot
#mpl.plot(seldf)
#mpl.show()

#CREATE TIME SERIES
import numpy as np
np.random.seed(0)
date_rng = pd.date_range(start="2021-01-01", periods=30*24, freq="D")
data = np.array(seldf)   #Put obj pandas to numpy
ts = pd.Series(data, index=date_rng)
print(ts)

#DECOMPOSITION
#pip install statsmodels
from statsmodels.tsa.seasonal import seasonal_decompose
dec_result = seasonal_decompose(data, model='additive',period=24)
dec_result.plot()