#Use r before the string for it to read the backslashes correctly
#Otherwise it tries to interpret them as formatting
#, encoding = 'utf-16' is for the encoding and making sure their isnt any weird characters
#TTTTTTTTTTTTTTTTTT
#This current checks to see what lines are missing from z in comparision to y
import os 

def fileCheck(u,o):
    with open(u, "r", encoding='utf-8') as file:
        lines = file.readlines()
    with open(o, "r", encoding='utf-8') as file2:
        lines2 = file2.readlines()
    for line2 in lines2:
        x = line2.strip()
        exists = False
        for line in lines:
            a = line.strip()
            if x == a:
                exists = True
        if(not exists):    
            print("Item located on line " +  x + " in " + o + " does not exist in " + u)

def patterncheck(u,o):
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
        print("The pattern does exists on line " + str(locate))
    else:
        print("The pattern does not exist")

def verifyfile(u):
    if os.path.isfile(u):
        print("The file exists")
    else:
        print("The file does not exist")
        with open(u, "w", encoding='utf-8') as file:
            file.write("This is a new file")

#z=r"C:\MattScript\Test.txt"
#y=r"C:\MattScript\File2.txt"
def run ():
    z = input("Type file path to check: ")
    y = input("Type file path to check against: ")
    verifyfile(z)
    verifyfile(y)
    fileCheck(z,y)
    fileCheck(y,z)
    pattern = input("Type pattern to check for: ")
    patterncheck(z, pattern)
    patterncheck(y, pattern)

run()