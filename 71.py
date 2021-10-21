import numpy as np
import matplotlib.pyplot as plt

with open("/home/gr101/Desktop/Scripts/1/settings.txt", "r") as settings:
    tmp=[str(i) for i in settings.read().split("\n")]
print(tmp[1])
data_array=np.loadtxt("/home/gr101/Desktop/Scripts/1/data.txt", dtype=float)
plt.figure()
fig, ax= plt.subplots(figsize=(16,10), dpi=400)
data_array=data_array*(3.3/255)
xlist = []
for i in range(0,len(data_array)):
    xlist.append(i*float(tmp[1])/(len(data_array)-1))
    print(xlist[i])

plt.plot(xlist,data_array)

plt.grid() 
#plt.xlabel("$Время,$ $с$")
ax.set_xlabel('Rotational period (hrs)')
#plt.ylabel("$Напряжение, B$")
ax.set_ylabel('Orbital radius (km), logarithmic')
plt.title("$Процесс$ $в$ $RC-цепи$")
plt.show()
fig.savefig('knkn.png')