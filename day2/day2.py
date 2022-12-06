with open("data.txt") as data:
    score = 0
    for line in data:
        code = line.replace("\n", "")
        match code:
            case "A X":
                score += (0 + 3)
            case "A Y":
                score += (3 + 1)
            case "A Z":
                score += (6 + 2)

                
            case "B X":
                score += (0 + 1)
            case "B Y":
                score += (3 + 2)
            case "B Z":
                score += (6 + 3)

                
            case "C X":
                score += (0 + 2)
            case "C Y":
                score += (3 + 3)
            case "C Z":
                score += (6 + 1)

    print(score)