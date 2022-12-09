from functools import reduce
import json
import operator

dirSize = dict()
total = 0
grandTotal = 0

iterator = 0

def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)

def setInDict(dataDict, mapList, value):
    getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value

def calculateDict(d):
    global total
    for k, v in d.items():
        if isinstance(v, dict):
            calculateDict(v)
        else:
            total += int(v)

def calculateMaxSize(d, maxSize):
    global total, grandTotal
    for k, v in d.items():
        if isinstance(v, dict):
            total = 0
            calculateDict(v)
            if total < maxSize:
                grandTotal += total
            calculateMaxSize(v, maxSize)

def calculateAllSize(d):
    global total, dirSize, iterator
    for k, v in d.items():
        if isinstance(v, dict):
            total = 0
            calculateDict(v)
            if k in dirSize:
                dirSize[k + "_" + str(iterator)] = total
                iterator += 1
            else:
                dirSize[k] = total
            calculateAllSize(v)

def getFileSystem():
    output = []
    filesys = dict()
    filesys["/"] = dict()
    with open("day7/data.txt") as data:
        for line in data:
            output.append(line.replace("\n", ""))
    path = []
    for line in output:
        command = line.split(" ")
        if command[0] == "$":
            match(command[1]):
                case "ls":
                    pass
                case "cd":
                    if command[2] == "..":
                        path.pop()
                    else:
                        path.append(command[2])
                        setInDict(filesys, path, dict())
        elif command[0].isdigit():
            setInDict(filesys, path + [command[1]], command[0])
    return filesys

def main():
    filesys = getFileSystem()
    calculateMaxSize(filesys, 100000)
    print("Part 1:", grandTotal)
    calculateAllSize(filesys)

    totalSize = 70000000
    updateSize = 30000000
    freeSpace = totalSize - dirSize["/"]
    spaceRequired = updateSize - freeSpace

    calculateDict(filesys["/"])

    smallestButBigEnough = ["x", 99**99]

    for dir, size in dirSize.items():
        if size > spaceRequired and size < smallestButBigEnough[1]:
            smallestButBigEnough = [dir, size]

    print("Part 2:", smallestButBigEnough[1])

if __name__ == "__main__":
    main()