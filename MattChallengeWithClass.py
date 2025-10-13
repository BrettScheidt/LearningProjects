import os 
import tkinter as tk

Comp = tk.Tk()
Comp.title("THE COMPARINATOR")
Comp.geometry("750x400")
global x
global y

def Compare_click():
    x=file1.get()
    y=file2.get()
    Comparinator.fileCheck(x,y)
    Comparinator.fileCheck(y,x)

def Pattern_click():
    x=file1.get()
    y=file2.get()
    pattern=patternt.get()
    Comparinator.patterncheck(x,pattern)
    Comparinator.patterncheck(y,pattern)
compare = tk.Button(Comp, text="Compare", command= Compare_click, width= 10, height=2) #, padx=17, pady=10
compare.place(x=305, y=50)
Pattern = tk.Button(Comp, text="Pattern Find", command= Pattern_click, width= 10, height=2) #, padx=17, pady=10
Pattern.place(x=305, y=100)

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


class Comparinator:
 #   def __init__(self):
 #       self.run()
    def fileCheck(u,o):
        
        if(Comparinator.verifyfile(u) and Comparinator.verifyfile(o)):
            with open(u, "r", encoding='utf-8') as file:
                lines = file.readlines()
            with open(o, "r", encoding='utf-8') as file2:
                lines2 = file2.readlines()
            count = 0
            for line2 in lines2:
                x = line2.strip()
                exists = False
                for line in lines:
                    a = line.strip()
                    if x == a:
                        exists = True
                if(not exists): 
                    Log.insert(0, "Item located on line " +  str(count) + " in " + o + " does not exist in " + u)
                    #print("Item located on line " +  str(count) + " in " + o + " does not exist in " + u)
                count += 1
        else:
            Log.insert(0, "One or both Files do not exist")

    def patterncheck(u,o):
        if os.path.isfile(u):
            with open(u, "r", encoding='utf-8') as file:
                lines = file.readlines() 
            exists = False  
            count = -1
            for line in lines:
                count += 1
                x = line.strip()
                if o in x:
                    exists = True
                    locate = count
            if(exists):
                Log.insert(0,"The pattern does exists on line " + str(locate))
                #print("The pattern does exists on line " + str(locate))
            else:
                Log.insert(0, "The pattern " + o + " does not exist")
                #print("The pattern does not exist")
        else:
            print("The file does not exist")
            Log.insert(0,"File: " + u + " Does not exist")
    def verifyfile(u):
        if os.path.isfile(u):
            print("The file exists")
            return True
        else:
            print("The file does not exist")
            return False
            with open(u, "w", encoding='utf-8') as file:
                file.write("This is a new file")

#app = Comparinator()
Comp.mainloop()