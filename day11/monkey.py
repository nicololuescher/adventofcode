import queue
import math

class Monkey:
    def __init__(self, items = []):
        self.items = queue.Queue()
        self.operation = None
        for item in items:
            self.items.put(item)
        self.inspections = 0
    
    def evaluate_items(self, monkeys, worried = False):
        while not self.items.empty():
            self.inspections += 1
            item = self.items.get()
            worry_level = self.evaluate(item)
            if not worried:
                worry_level = math.floor(worry_level / 3)
            if(self.test(worry_level)):
                monkeys[self.true_monkey].give_item(worry_level % self.lcm)
            else:
                monkeys[self.false_monkey].give_item(worry_level % self.lcm)
    
    def get_item(self):
        return self.items.get()
    
    def give_item(self, item):
        self.items.put(item)
    
    def set_operation(self, operation):
        self.operation = operation
    
    def set_test(self, test):
        self.divisor = int(test)
    
    def set_lcm(self, lcm):
        self.lcm = int(lcm)
    
    def set_true_monkey(self, monkey):
        self.true_monkey = int(monkey)
        
    def set_false_monkey(self, monkey):
        self.false_monkey = int(monkey)
    
    def evaluate(self, old):
        calculation = []
        for entry in [self.operation[0], self.operation[2]]:
            if entry.isdigit():
                calculation.append(int(entry))
            else:
                calculation.append(old)
        if self.operation[1] == "+":
            return calculation[0] + calculation[1]
        elif self.operation[1] == "*":
            return calculation[0] * calculation[1]
    
    def test(self, value):
        return value % self.divisor == 0