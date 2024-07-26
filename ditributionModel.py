# Hairong Wang; hairongw; 12746; A

import tkinter as tk
from tkinter import *
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


# density of each phase Kg/m3
dens = {'air': 1.19, 'water': 1000, 'soil': 1000, 'sedi': 1500, 'bio': 1000}
# molar weight g/mol
mw = {'Benzene': 78.11, 'Chlorobenzene': 112.6, 'PCB': 223.1, 'DEHP': 390.54, 'Aniline': 93.12, 'DDT': 354.5}
# vapor pressure Pa
vp = {'Benzene': 1.27e4, 'Chlorobenzene': 1.58e3, 'PCB': 4.8e-3, 'DEHP': 1.33e-5, 'Aniline': 65.2, 'DDT': 2e-5}
# solubility in water g/m3
sl = {'Benzene': 1780, 'Chlorobenzene': 484, 'PCB': 0.06, 'DEHP': 0.285, 'Aniline': 36070, 'DDT': 5.5e-3}
# octanol-water partitioning factor
Kow = {'Benzene': 134.89, 'Chlorobenzene': 630.96, 'PCB': 1.995e5, 'DEHP': 1.288e5, 'Aniline': 7.94, 'DDT': 1.549e6}
# air-water distribution factor
Kiaw = {'Benzene': 0.2248, 'Chlorobenzene': 0.1438, 'PCB': 7.2e-3, 'DEHP': 7.352e-6, 'Aniline': 6.791e-5, 'DDT': 5.2e-4}
# soil-water partitioning factor
Kid = {'Benzene': 2.55, 'Chlorobenzene': 11.9, 'PCB': 3.77e3, 'DEHP': 2.43e3, 'Aniline': 0.15, 'DDT': 2.93e4}
# sediment-water partitioning factor
Kisd = {'Benzene': 5.1, 'Chlorobenzene': 23.9, 'PCB': 7.54e3, 'DEHP': 4.87e3, 'Aniline': 0.3, 'DDT': 5.85e4}
# biota-water partitioning factor
BCF = {'Benzene': 27, 'Chlorobenzene': 126, 'PCB': 3.99e4, 'DEHP': 2.58e4, 'Aniline': 1.59, 'DDT': 3.1e5}


# distribution function and mass fraction output
def dis(Vw, Va, Vs, Vsed, Vbio, x):
    fw = Vw/(Va*int(Kiaw[x])+Vw+Vs*int(Kid[x])+Vsed*int(Kisd[x])+Vbio*int(BCF[x]))
    fa = Va*int(Kiaw[x])/(Va*int(Kiaw[x])+Vw+Vs*int(Kid[x])+Vsed*int(Kisd[x])+Vbio*int(BCF[x]))
    fs =Vs*int(Kid[x])/(Va*int(Kiaw[x])+Vw+Vs*int(Kid[x])+Vsed*int(Kisd[x])+Vbio*int(BCF[x]))
    fsd = Vsed*int(Kisd[x])/(Va*int(Kiaw[x])+Vw+Vs*int(Kid[x])+Vsed*int(Kisd[x])+Vbio*int(BCF[x]))
    fb = Vbio*int(BCF[x])/(Va*int(Kiaw[x])+Vw+Vs*int(Kid[x])+Vsed*int(Kisd[x])+Vbio*int(BCF[x]))
    f = [fw, fa, fs, fsd, fb]

# pie chart
    labels = ['water', 'air', 'soil', 'sediment', 'biota']
    fig = plt.figure()
    plt.pie(f, labels=labels, autopct='%1.2f%%')
    plt.title("Organic Mass Distribution")
    plt.show()


# display organic data
def show(i):
    a = 'Organic name: %s\n Molar weight: %.4f g/mol\n Vapor pressure: %.4f Pa\n Solubility in water: %.4f g/m3\n' \
        ' Octanol-water factor Kow: %.4f\n air-water factor Kiaw: %.4f\n soil-water factor Kid: %.4f\n' \
        ' sediment-water factor Kisd: %.4f\n biota-water factor BCF: %.4f' %(i, mw[i], vp[i], sl[i], Kow[i], Kiaw[i], Kid[i], Kisd[i], BCF[i])
    text.insert(END, a, 'end', '\n')
    Va = int(e1.get())
    Vw = int(e2.get())
    Vs = int(e3.get())
    Vsed = int(e4.get())
    Vbio = int(e5.get())
    dis(Vw, Va, Vs, Vsed, Vbio, i)


# help to clean the window
def delete():
    text.delete(1.0, END)


# GUI
wd = tk.Tk()

# window size
wd.geometry('610x400')

# window name
wd.title("Organic Distribution Model")

# entry for volume input
volume =['Volume of air', 'Volume of water', 'Volume of soil', 'Volume of sediment', 'Volume of biota']
r = 0
for v in volume:
    Label(text=v, relief=RIDGE, width=15).place(x=150, y=30 + r*30, width=120, height=25)
    r += 1

# default value
v1 = IntVar()
v1.set(100000)
v2 = IntVar()
v2.set(5000)
v3 = IntVar()
v3.set(10000)
v4 = IntVar()
v4.set(1000)
v5 = IntVar()
v5.set(100)

e1 = tk.Entry(text=v1)
e1.place(x=350, y=30)
e2 = tk.Entry(text=v2)
e2.place(x=350, y=60)
e3 = tk.Entry(text=v3)
e3.place(x=350, y=90)
e4 = tk.Entry(text=v4)
e4.place(x=350, y=120)
e5 = tk.Entry(text=v5)
e5.place(x=350, y=150)


# text for display
text = tk.Text(wd, height=10)
text.place(x=20, y=200)

# button for clear the text
button = tk.Button(wd, text='Clear', command=delete)
button.place(x=150, y=350)


# organic choose menu
menuBar = Menu(wd)
menuA = Menu(menuBar, tearoff=False)
menuA.add_command(label='Benzene', command=lambda: show('Benzene'))
menuA.add_command(label='Chlorobenzene', command=lambda: show('Chlorobenzene'))
menuA.add_command(label='PCB', command=lambda: show('PCB'))
menuA.add_command(label='DEHP', command=lambda: show('DEHP'))
menuA.add_command(label='Aniline', command=lambda: show('Aniline'))
menuA.add_command(label='DDT', command=lambda: show('DDT'))
menuBar.add_cascade(label='choose organic', menu=menuA)


# button for quit
button = tk.Button(wd, text='Quit', command=wd.quit)
button.place(x=450, y=350)

wd.config(menu=menuBar)
wd.mainloop()