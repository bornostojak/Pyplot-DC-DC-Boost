#!/bin/python3
from matplotlib import pyplot as plt


fig, gnt = plt.subplots()

tx=["\n10.10.2019.", "16.10.2019.", "\n3.11.2019.", "9.11.2019.", "\n\n15.1.2020.", "\n16.1.2020.", "20.1.2020."]
ty=["Shema i tlocrt\npločice, BOM", "Kontrola dizajna\ni korekcije,\nslanje na izradu.", "Predaja Plana projekta", "Sastavljanje pločice", "Testiranje pločice", "Primopredaja projekta"]
gnt.set_xlabel("Datumi")
gnt.set_ylabel("Obaveze")

a=6
b=24
c=30
d=97
e=98
f=102
tata=[0, a, b, c, d, e, f]

ll=[None]*106
print(len(ll))
for ii in range(len(tata)):
    ll[tata[ii]]=tx[ii]

print("Result: "+ str(len(tata)-len(tx)))

gnt.set_xticks(range(106))
gnt.set_xticklabels(ll)



yoffset=-0.25
yheight=0.5

gnt.broken_barh([(a, b-a )], (0+yoffset, yheight), facecolors=('tab:orange'))
gnt.broken_barh([(b, c-b)], (1+yoffset, yheight), facecolors=('tab:blue'))
gnt.broken_barh([(c, d-c)], (2+yoffset, yheight), facecolors=('tab:green'))
gnt.broken_barh([(d, e-d)], (3+yoffset, yheight), facecolors=('tab:purple'))
gnt.broken_barh([(e, f-e)], (4+yoffset, yheight), facecolors=('tab:pink'))
gnt.broken_barh([(f, 106-f)], (5+yoffset, yheight), facecolors=('tab:red'))



gnt.set_yticks(range(len(ty)))
gnt.set_yticklabels(ty)

plt.plot()
plt.show()
