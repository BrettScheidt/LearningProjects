import os 
import tkinter as tk

class Comparinator:
 #   def __init__(self):
 #       self.run()

    def Compare_click(file1,file2,Log):
        x=file1.get()
        y=file2.get()
        Comparinator.fileCheck(x,y, Log)
        Comparinator.fileCheck(y,x, Log)

    def Pattern_click(file1,file2,patternt,Log):
        x=file1.get()
        y=file2.get()
        pattern=patternt.get()
        Comparinator.patterncheck(x,pattern, Log)
        Comparinator.patterncheck(y,pattern, Log)
    
    def fileCheck(u,o, Log):
        
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

    def patterncheck(u,o, Log):
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
                Log.insert(0,"The pattern does exists on line " + str(locate) + " in file: " + u)
                #print("The pattern does exists on line " + str(locate))
            else:
                Log.insert(0, "The pattern " + o + " does not exist on file: " + u)
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
            
            #with open(u, "w", encoding='utf-8') as file:
            #    file.write("This is a new file")
            return False