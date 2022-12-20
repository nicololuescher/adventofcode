def getData(path):
    returnArray = []
    with open(path) as data:
        for line in data:
            row = []
            for digit in line.replace("\n", "").replace(" ", ""):
                row.append(digit)
            returnArray.append(row)
    return returnArray

def isTop(y):
    return y == 0

def isBottom(trees, y):
    return y == len(trees) - 1

def isLeft(x):
    return x == 0

def isRight(trees, x):
    return x == len(trees[0]) - 1

def isEdge(trees, x, y):
    return isTop(y) or isBottom(trees, y) or isLeft(x) or isRight(trees, x)

def isVisible(trees, x, y):
    directionsInvisible = 0
    if isEdge(trees, x, y):
        return True
    
    # up
    for i in range(y):
        if trees[x][i] >= trees[x][y]:
            directionsInvisible += 1
            break

    # down
    for i in range(len(trees) - 1 - y):
        if trees[x][y + i + 1] >= trees[x][y]:
            directionsInvisible += 1
            break

    # left
    for i in range(x):
        if trees[i][y] >= trees[x][y]:
            directionsInvisible += 1
            break
    
    # right
    for i in range(len(trees[x]) - 1 - x):
        if trees[x + i + 1][y] >= trees[x][y]:
            directionsInvisible += 1
            break

    return not directionsInvisible == 4

def getScenicScore(trees, x, y):
    scores = [0,0,0,0]
    
    # up
    if not isTop(y):
        for i in reversed(range(y)):
            if trees[x][i] >= trees[x][y]:
                scores[0] = scores[0] + 1
                break
            else:
                scores[0] += 1

    # down
    if not isBottom(trees, y):
        for i in range(len(trees) - 1 - y):
            if trees[x][y + i + 1] >= trees[x][y]:
                scores[1] = scores[1] + 1
                break
            else:
                scores[1] += 1

    # left
    if not isLeft(x):    
        for i in reversed(range(x)):
            if trees[i][y] >= trees[x][y]:
                scores[2] = scores[2] + 1
                break
            else:
                scores[2] += 1
    
    # right
    if not isRight(trees, x):
        for i in range(len(trees[x]) - 1 - x):
            if trees[x + i + 1][y] >= trees[x][y]:
                scores[3] = scores[3] + 1
                break
            else:
                scores[3] += 1
    total = 1
    for score in scores:
        total *= score
    return total

def main():
    trees = getData("day8/data.txt")
    total = 0

    for x in range(len(trees)):
        for y in range(len(trees[0])):
            if isVisible(trees, x, y):
                total += 1
    print("Part 1: ", total)

    currentBest = 0

    for x in range(len(trees)):
        for y in range(len(trees[0])):
            if getScenicScore(trees, x, y) > currentBest:
                currentBest = getScenicScore(trees, x, y)
    print("Part 2: ", currentBest)


if __name__ == "__main__":
    main()