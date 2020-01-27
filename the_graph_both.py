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
    
def PrintPlot(theData, loc, mode):
    plt.subplot(loc)
    plt.title("Efficiency vs Output Current ("+mode+" mode)")
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.xscale("log")
    plt.yticks(np.array(range(0, 111, 10)))
    plt.xticks([0.05, 0.01, 0.2, 0.5, 0.1, 1.0, 2.0, 3.0, 4.0, 5.0], [0.05, 0.01, 0.2, 0.5, 0.1, 1.0, 2.0, 3.0, 4.0, 5.0])
    plt.grid(b=True, which="both", axis="both")
    for d in range(len(theData)):
        plt.plot(theData[d].x, theData[d].y, color=color[d], label=str(theData[d].voltage))
    plt.legend()

labelx="Output Current [A]"  
labely="Efficiency [%]"
data=[]
color=["r", "g", "b", "k"]

with open(str(sys.argv[1]), "r")as csvfile:
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
    PrintPlot(data, 121, sys.argv[2])
data=[]
with open(str(sys.argv[3]), "r")as csvfile:
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
    PrintPlot(data, 122, sys.argv[4])

plt.show()
