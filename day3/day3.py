def getValue(c):
    if c.islower():
        return int(ord(c.upper()) - 64)
    else:
        return int(ord(c.upper()) - 64 + 26)

with open("data.txt") as rucksack:
    total = 0
    for line in rucksack:
        content = line.replace("\n", "")
        first = content[:int(len(content)/2)]
        second = content[int(len(content)/2):]

        for c in first:    
            if c in second:
                total += getValue(c)
                break

    print(i)
    print(total)

with open("data.txt") as rucksack:
    total = 0
    rucksacks = rucksack.read().split("\n")
    for i in range(int(len(rucksacks) / 3)):
        group = rucksacks[i * 3: i * 3 + 3]
        for c in group[0]:
            if c in group[1] and c in group[2]:
                print(c)
                total += getValue(c)
                break
    print(total)