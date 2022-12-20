def get_data(path):
    with open(path) as f:
        result = []
        for line in f:
            result.append([])
            for char in line.strip():
                result[-1].append(ord(char))
    return result

def get_start_and_end(data):
    start = None
    end = None
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] == 83:
                start = (x, y)
            if data[x][y] == 69:
                end = (x, y)
    return start, end

def main():
    data = get_data("day12/test_data.txt")
    start, end = get_start_and_end(data)
    print(data)
    print(start, end)
    return

if __name__ == "__main__":
    main()
