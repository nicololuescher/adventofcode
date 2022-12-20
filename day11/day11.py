from monkey import Monkey

def get_data(path):
    result = []
    with open(path, "r") as f:
        for line in f.read().splitlines():
            result.append(line.strip().replace(",", "").split(" "))
    return result

def main():
    data = get_data("day11/test_data.txt")    
    monkeys = []
    
    for line in data:
        if line[0] == "Monkey":
            monkeys.append(Monkey())
            
        if line[0] == "Starting":
            for item in line[2:]:
                monkeys[-1].give_item(item)
        
        if line[0] == "Operation:":
            monkeys[-1].set_operation(line[line.index("=") + 1:])
            
        if line[0] == "Test:":
            monkeys[-1].set_test(line[-1])
           
        if line[0] == "If": 
            if line[1] == "true:":
                monkeys[-1].set_true_monkey(line[-1])
                
            if line[1] == "false:":
                monkeys[-1].set_false_monkey(line[-1])
    return

if __name__ == "__main__":
    main()