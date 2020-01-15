#!/bin/python3

import csv
import matplotlib.pyplot as plt
import numpy as np
import sys

class Data:
    def __init__(self, classname, voltage):
        self.name=classname
        self.x=[]
        self.y=[]
        self.name=""
        self.mode=""
        self.voltage=voltage
    
mode=sys.argv[2]
labelx="Output Current [A]"  
labely="Efficiency [%]"
data=[]
color=["r", "g", "b", "k"]

with open(str(sys.argv[1]), "r")as csvfile:           #"/home/graveface/MEGAsync/LibreDocuments/Project_DC-DC-Boost/C/Efficiency-DC-Converter-FPWM.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    current=None
    for row in reader:
        if row["Name"]!="":
            current = Data(row["Name"], row["Voltage"])
            data.append(current)
        elif row["Mode"]!="":
            current.mode = row["Mode"]
        elif row["Output Current"]!="" and row["Efficiency"]!="":
            current.x.append(float(row["Output Current"]))
            current.y.append(float(row["Efficiency"]))

fig=plt.figure()
fig.set_size_inches(10.0, 5.0)

plt.subplot(121)
plt.title("Efficiency vs Output Current ("+mode+" mode)")
plt.xlabel(labelx)
plt.ylabel(labely)
plt.xscale("log")
plt.yticks(np.array(range(0, 111, 10)))
plt.xticks([0.05, 0.01, 0.2, 0.5, 0.1, 1.0, 2.0, 3.0, 4.0, 5.0], [0.05, 0.01, 0.2, 0.5, 0.1, 1.0, 2.0, 3.0, 4.0, 5.0])
plt.grid(b=True, which="both", axis="both")
for d in range(len(data)):
    plt.plot(data[d].x, data[d].y, color=color[d], label=str(data[d].voltage))
plt.legend()


plt.subplot(122)
plt.title("Efficiency vs Output Current ("+mode+" mode, linear)")
plt.xlabel(labelx)
plt.ylabel(labely)
plt.yticks(np.array(range(0, 111, 10)))
#plt.xticks([0.05, 0.01, 0.2, 0.5, 0.1, 1.0, 2.0, 3.0, 4.0, 5.0], [0.05, 0.01, 0.2, 0.5, 0.1, 1.0, 2.0, 3.0, 4.0, 5.0])
plt.xticks([1.0, 1.5,  2.0, 2.5, 3.0, 3.5, 4.0, 4.5] , [1.0, 1.5,  2.0, 2.5, 3.0, 3.5, 4.0, 4.5])
plt.grid(b=True, which="both", axis="both")
for d in range(len(data)):
    plt.plot(data[d].x, data[d].y, color=color[d], label=data[d].voltage)
plt.legend()

plt.show()
