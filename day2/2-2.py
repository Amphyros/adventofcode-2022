from input import input

def getInputValue(input) -> int:
    match input:
        case 'A':
            return 1
        case 'B':
            return 2
        case 'C':
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

def getResponseBasedOnResult(opponentValue: int, result):
    response = None

    match result:
        case 'X':
            response = opponentValue - 1
        case 'Y':
            return opponentValue
        case 'Z': 
            response = opponentValue + 1
    
    if response == 4:
        response = 1
    if response == 0:
        response = 3
    return response


score = 0

for match in input.splitlines():
    elf = match[0]
    result = match[2]
    
    response = getResponseBasedOnResult(getInputValue(elf), result)
    score += getMatchScore(getInputValue(elf), response) + response
    
print(score)
