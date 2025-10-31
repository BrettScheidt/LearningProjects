import os 
import tkinter as tk
import BackEndTest as ms

Comp = tk.Tk()
Comp.title("THE COMPARINATOR")
Comp.geometry("750x400")

def compare_submit():
    ms.Comparinator.Compare_click(file1,file2,Log)
def pattern_submit():
    ms.Comparinator.Pattern_click(file1,file2,patternt,Log)


file1 = tk.Entry(Comp, width=30)
file1.place(x=100,y=75)
file2 = tk.Entry(Comp, width=30)
file2.place(x=400,y=75)
patternt = tk.Entry(Comp, width=30)
patternt.place(x=260,y=200)

File1Title = tk.Label(Comp, text="File 1:")
File1Title.place(x=100, y=55)
File2Title = tk.Label(Comp, text="File 2:")
File2Title.place(x=400, y=55)
PatternTitle = tk.Label(Comp, text="Pattern:")
PatternTitle.place(x=260, y=180)

Dlist = tk.Label(Comp, text="Results")
Dlist.place(x=10, y=250)
Log = tk.Listbox(Comp, width=110, height=8)
Log.place(x=10, y=270)

compare = tk.Button(Comp, text="Compare", command= compare_submit, width= 10, height=2) #, padx=17, pady=10
compare.place(x=305, y=50)
Pattern = tk.Button(Comp, text="Pattern Find", command= pattern_submit, width= 10, height=2) #, padx=17, pady=10
Pattern.place(x=305, y=100)


Comp.mainloop()