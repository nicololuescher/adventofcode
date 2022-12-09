def main():
    input = open("day6/data.txt").read().replace(" ", "").replace("\n", "")
    i = 0
    buffer = []
    for c in input:
        i += 1
        if len(buffer) > 3:
            buffer = buffer[1:]
            buffer.append(c)
            if(len(buffer) == len(set(buffer))):
                print("Part 1:", i)
                break
        else:
            buffer.append(c)

    buffer = []
    i = 0
    for c in input:
        i += 1
        if len(buffer) > 13:
            buffer = buffer[1:]
            buffer.append(c)
            if(len(buffer) == len(set(buffer))):
                print("Part 2:", i)
                break
        else:
            buffer.append(c)
            
if __name__ == "__main__":
    main()