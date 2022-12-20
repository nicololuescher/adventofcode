import math

def get_data(path):
    with open(path) as data_file:
        returnList = []
        for line in data_file:
            returnList.append(line.strip().split(" "))
        return returnList

def draw_pixel(counter, x, crt):    
    array_position = math.floor((counter - 1) / 40)
    if(len(crt) <= array_position):
        crt.append([])
        
    if (counter - 1) % 40 >= x - 1 and (counter - 1) % 40 <= x + 1:
        crt[array_position].append("#")
    else:
        crt[array_position].append(".")
    return crt

def evaluate(instruction, counter, x, total, crt):
    crt = draw_pixel(counter, x, crt)
    if((counter + 20) % 40 == 0):
        # print(counter, x, counter * x, total)
        total += counter * x
    if instruction[0] == "noop":
        return counter + 1, x, total, crt
    elif instruction[0] == "addx":
        counter += 1
        return evaluate(["addc", instruction[1]], counter, x, total, crt)
    elif instruction[0] == "addc":
        x += int(instruction[1])
        counter += 1
        return counter, x, total, crt

def main():
    instructions = get_data("day10/data.txt")
    #instructions = get_data("day10/test_data.txt")
    counter = 1
    x = 1
    total = 0
    crt = []
    for instruction in instructions:
        counter, x, total, crt = evaluate(instruction, counter, x, total, crt)
    print(total)
    for line in crt:
        print("".join(line))

if __name__ == "__main__":
    main()