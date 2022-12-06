with open("data.txt") as data:
    elvs = []
    elv = 0
    for line in data:
        if line == "\n":
            elvs.append(elv)
            elv = 0
        else:
            elv += int(line[:-1])
    elvs.sort()
    print(sum(elvs[-3:]))