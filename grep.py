import os
import sys

print(sys.argv)

args = sys.argv

'''searchString = ""

if len(args) > 1:
    for index in range(1,len(args)):
        searchString += args[index] + ' '

print(searchString)
'''

word = args[1]

files = []
searchString = ""
file = ""
if len(args) > 2:
    for index in range(2,len(args)):
        file = args[index]
        files.append(file)
        #files += args[index] lägger in varje char för sig istället för ett helt arg.
        print(args[index])
        searchString += args[index] + ' '


print(word)
print(files)
#print(searchString)

filename = "example.txt"

if os.path.isfile(filename):
    print(f"'{filename}' is a file.")
else:
    print(f"'{filename}' is not a file.")

for file in files:
    if os.path.isfile(file):
        rowCount = 0
        with open(file, "r") as fileHandler:
            for line in fileHandler:
                rowCount += 1
                if word in line:
                    print("Found word in " + file + " at line "+ str(rowCount) + ": " + line)
                    
                    
        fileHandler.close()
    
    else:
        print(file + " does not exist.")