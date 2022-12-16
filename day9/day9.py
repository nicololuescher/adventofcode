xExtreme = [0,0]
yExtreme = [0,0]

def getData():
    with open('day9/data.txt') as f:
        data = []
        for lines in f.readlines():
            data.append(lines.replace("\n", "").split(" "))
    return data

def visualize(rope):
    for knot in rope:
        if knot[0] < xExtreme[0]:
            xExtreme[0] = knot[0]
        elif knot[0] > xExtreme[1]:
            xExtreme[1] = knot[0]
        
        if knot[1] < yExtreme[0]:
            yExtreme[0] = knot[1]
        elif knot[1] > yExtreme[1]:
            yExtreme[1] = knot[1]
    for y in reversed(range(yExtreme[0], yExtreme[1] + 1)):
        for x in range(xExtreme[0], xExtreme[1] + 1):
            if (x,y) in rope:
                print(rope.index((x,y)) % 10, end="")
            elif (x,y) == (0,0):
                print("X", end="")
            else:
                print(".", end="")
        print("")
    print("")
            

def move(position, direction):
    if direction == 'U':
        return (position[0], position[1] + 1)
    elif direction == 'R':
        return (position[0] + 1, position[1])
    elif direction == 'D':
        return (position[0], position[1] - 1)
    elif direction == 'L':
        return (position[0] - 1, position[1])
    return position

def moveTail(difference):
    if difference[0] == 0 and difference[1] == 2:
        return (0, 1)
    elif difference[0] == 1 and difference[1] == 2:
        return (1, 1)
    elif difference[0] == 2 and difference[1] == 2:
        return (1, 1)
    elif difference[0] == 2 and difference[1] == 1:
        return (1, 1)
    elif difference[0] == 2 and difference[1] == 0:
        return (1, 0)
    elif difference[0] == 2 and difference[1] == -1:
        return (1, -1)
    elif difference[0] == 2 and difference[1] == -2:
        return (1, -1)
    elif difference[0] == 1 and difference[1] == -2:
        return (1, -1)
    elif difference[0] == 0 and difference[1] == -2:
        return (0, -1)
    elif difference[0] == -1 and difference[1] == -2:
        return (-1, -1)
    elif difference[0] == -2 and difference[1] == -2:
        return (-1, -1)
    elif difference[0] == -2 and difference[1] == -1:
        return (-1, -1)
    elif difference[0] == -2 and difference[1] == 0:
        return (-1, 0)
    elif difference[0] == -2 and difference[1] == 1:
        return (-1, 1)
    elif difference[0] == -2 and difference[1] == 2:
        return (-1, 1)
    elif difference[0] == -1 and difference[1] == 2:
        return (-1, 1)
    return (0,0)

def main():
    steps = getData()
    # steps = [
    #     ["R", 5],
    #     ["U", 8], 
    #     ["L", 8], 
    #     ["D", 3], 
    #     ["R", 17], 
    #     ["D", 10], 
    #     ["L", 25], 
    #     ["U", 20]
    #     ]
    # steps = [["U", 5], ["R", 4]]
    head = (0,0)
    tail = (0,0)
    longRope = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
    visited = []
    longVisited = []
    for step in steps:
        for i in range(int(step[1])):
            head = move(head, step[0])
            tailDiff = moveTail((head[0] - tail[0], head[1] - tail[1]))
            tail = (tail[0] + tailDiff[0], tail[1] + tailDiff[1])
            
            longRope[0] = move(longRope[0], step[0])
            for j in range(1, len(longRope)):
                diff = moveTail((longRope[j-1][0] - longRope[j][0], longRope[j-1][1] - longRope[j][1]))
                longRope[j] = (longRope[j][0] + diff[0], longRope[j][1] + diff[1])
            
            if tail not in visited:
                visited.append(tail)
                
            if longRope[9] not in longVisited:
                longVisited.append(longRope[9])
    print(len(visited))
    print(len(longVisited))
    return 0

if __name__ == "__main__":
    main()