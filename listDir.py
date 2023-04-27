import os
import sys

print(sys.argv)

# get the current working directory
cwd = os.getcwd()

args = sys.argv





print("\nDirectory contents: ")

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

if len(args) == 2 and os.path.isdir(os.path.join(cwd, args[1])):
    dir = args[1]
    print(args[1] + " is a valid dir")
    listDir(cwd, dir)
else:
    listDir(cwd, 'magi')
    




# list all directories in the current working directory
#directories = [d for d in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, d))]

# print the list of directories
#print(directories)

#drs = os.listdir(cwd)

#print(drs)