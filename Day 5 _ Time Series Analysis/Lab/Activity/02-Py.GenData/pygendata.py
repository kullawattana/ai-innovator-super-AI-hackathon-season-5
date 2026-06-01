
#Create trend line
t = []
for i in range(0,100):
    t.append(i)
print(t)

#Create cyclic
import math
c = []
for i in range(0,100):
    c.append(math.sin(i/10)*2)
print(c)

#Create random
import random as ran
r = []
for i in range(0,100):
    if (ran.random() > 0.8):
        r.append(ran.random()*2)
    else:
        r.append(0)
print(r)


sig = []
for i in range(0,100):
  sig.append(t[i]+c[i]+r[i])

print(sig)

#Plot
import matplotlib.pyplot as mpl
mpl.clf()  #Clear plot
mpl.plot(range(0,100),sig)
mpl.show()


#Export to csv
import csv
with open('output.csv', 'w', newline = '\n') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ",")
    my_writer.writerow(sig)