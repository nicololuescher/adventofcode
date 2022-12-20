from monkey import Monkey
import numpy

def get_data(path):
    result = []
    with open(path, "r") as f:
        for line in f.read().splitlines():
            result.append(line.strip().replace(",", "").split(" "))
    return result

def generate_monkeys(data):
    monkeys = []
    devisor = 1
    
    for line in data:
        if line[0] == "Monkey":
            monkeys.append(Monkey())
            
        if line[0] == "Starting":
            for item in line[2:]:
                monkeys[-1].give_item(int(item))
        
        if line[0] == "Operation:":
            monkeys[-1].set_operation(line[line.index("=") + 1:])
            
        if line[0] == "Test:":
            devisor *= int(line[-1])
            monkeys[-1].set_test(line[-1])
           
        if line[0] == "If": 
            if line[1] == "true:":
                monkeys[-1].set_true_monkey(line[-1])
                
            if line[1] == "false:":
                monkeys[-1].set_false_monkey(line[-1])
    for monkey in monkeys:
        monkey.set_lcm(devisor)
    return monkeys
    

def main():
    #data = get_data("day11/test_data.txt")   
    data = get_data("day11/data.txt")    

    monkeys = generate_monkeys(data)
    monkey_business = []

    for i in range(20):
        for monkey in monkeys:
            monkey.evaluate_items(monkeys)
    for monkey in monkeys:
        monkey_business.append(monkey.inspections)
    monkey_business.sort()
    print("Task 1:", numpy.prod(monkey_business[-2:]))

    monkeys = generate_monkeys(data)
    monkey_business = []

    for i in range(10000):
        print(str(i) + "/10000", end="\r")
        for monkey in monkeys:
            monkey.evaluate_items(monkeys, True)
    for monkey in monkeys:
        monkey_business.append(monkey.inspections)
    monkey_business.sort()
    print("Task 2:", numpy.prod(monkey_business[-2:]))


if __name__ == "__main__":
    main()