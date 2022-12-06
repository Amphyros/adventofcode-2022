from input import input

def getResponseScore(response) -> int:
    match response:
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3
        case _:
            return 0

def getInputToInt(input) -> int:
    match input:
        case 'A':
            return 1
        case 'B':
            return 2
        case 'C':
            return 3
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3
        case _:
            return None

def getMatchScore(opponent, player) -> int:
    if player == opponent:
        return 3
    if player == (opponent + 1) or player == (opponent - 2):
        return 6
    if player == (opponent - 1) or player == (opponent + 2):
        return 0


score = 0

for match in input.splitlines():
    elf = match[0]
    response = match[2]

    score += getResponseScore(response) + getMatchScore(getInputToInt(elf), getInputToInt(response))

print(score)
