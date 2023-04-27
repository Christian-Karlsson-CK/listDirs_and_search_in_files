import os
import sys

def listDir(cwd, dir):
    for item in os.listdir(os.path.join(cwd, dir)):
        path = os.path.join(cwd, dir)
        if os.path.isdir(os.path.join(path, item)):
            #print("DIR: " + item)
            print(os.path.join(dir, item))
            newDir = os.path.join(dir, item)
            listDir(cwd, newDir)
        elif os.path.isfile(os.path.join(path, item)):
            #print("FILE: " + item)
            print(os.path.join(dir, item))
            searchFile(os.path.join(dir, item))

def searchFile(file):
    print("--------WORD SEARCH IN " + file + "----------")
    if os.path.isfile(file):
        rowCount = 0
        foundWord = False
        with open(file, "r") as fileHandler:
            for line in fileHandler:
                rowCount += 1
                if word in line:
                    foundWord = True
                    print("Found word in " + file + " at line "+ str(rowCount) + ": " + line)
         
        fileHandler.close()
        if not foundWord:
            print("The word was not found.")
    
    else:
        print(file + " does not exist.")

print(sys.argv)

args = sys.argv

cwd = os.getcwd()

word = args[1]
startFolder = args[2]

print(word)

if len(args) == 2 and os.path.isdir(os.path.join(cwd, args[1])):
    dir = args[1]
    print(args[1] + " is a valid dir")
    listDir(cwd, dir)
else:
    listDir(cwd, 'magi')



