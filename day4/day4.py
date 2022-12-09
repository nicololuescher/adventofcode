def check_full_overlap(first, second):
    return first.start >= second.start and first.stop <= second.stop or second.start >= first.start and second.stop <= first.stop

def check_overlap(first, second):
    return first.start <= second.start and first.stop >= second.start or second.start <= first.start and second.stop >= first.start

with open("day4/data.txt") as data:
    total = 0
    total_partial = 0
    for line in data:
        assignments = line.replace("\n", "").split(",")
        first = range(int(assignments[0].split("-")[0]), int(assignments[0].split("-")[1]))
        second = range(int(assignments[1].split("-")[0]), int(assignments[1].split("-")[1]))
        
        if check_full_overlap(first, second):
            total += 1
            
                
        if check_overlap(first, second):
            total_partial += 1
    print(total)
    print(total_partial)