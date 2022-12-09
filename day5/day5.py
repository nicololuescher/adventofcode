stack = [[], [], [], [], [], [], [], [], []]
stack2 = [[], [], [], [], [], [], [], [], []]
moves = []

with open("day5/data.txt") as data_file:
    for line in reversed(data_file.readlines()):
        for i in range(9):
            if not line.replace("\n", "")[i * 4 + 1: i * 4 + 2] == " ":
                stack[i].append(line.replace("\n", "")[i * 4 + 1: i * 4 + 2])
                stack2[i].append(line.replace("\n", "")[i * 4 + 1: i * 4 + 2])


with open("day5/moves.txt") as moves_file:
    for line in moves_file.readlines():
        moves.append([
            int(line.replace("\n", "").split(" ")[1]),
            int(line.replace("\n", "").split(" ")[3]),
            int(line.replace("\n", "").split(" ")[5])
            ])

for move in moves:
    for i in range(move[0]):
        element = stack[move[1] - 1].pop()
        stack[move[2] - 1].append(element)

for e in stack:
    print(e[len(e)-1], end="")
print()

for move in moves:
    elements = stack2[move[1] - 1][-move[0]:]
    stack2[move[1] - 1] = stack2[move[1] - 1][:-move[0]]
    for element in elements:
        stack2[move[2] - 1].append(element)

for e in stack2:
    print(e[len(e)-1], end="")
print()