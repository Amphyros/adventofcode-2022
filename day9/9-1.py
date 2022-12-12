from input import input

def getNewRopePositions(direction:int, head:list, tail:list) -> list:
    newHeadPosition = list(head)
    newTailPosition = list(tail)

    match direction:
        case "U":
            newHeadPosition[1] += 1
        case "R":
            newHeadPosition[0] += 1
        case "D":
            newHeadPosition[1] -= 1
        case "L":
            newHeadPosition[0] -= 1
    
    xDifference = abs(newHeadPosition[0] - tail[0])
    yDifference = abs(newHeadPosition[1] - tail[1])

    if xDifference >= 2 or yDifference >= 2:
        newTailPosition = list(head)
    
    return [newHeadPosition, newTailPosition]


def getUniqueTailPositions(input:str) -> int:
    headPosition = [0,0]
    tailPosition = [0,0]
    uniqueTailPositions = []
    uniqueTailPositions.append(list(tailPosition))

    for step in input.splitlines():
        splitStep = step.split()
        direction = splitStep[0]
        distance = int(splitStep[1])

        for _ in range(0, distance):
            newPositions = getNewRopePositions(direction, headPosition, tailPosition)
            headPosition = list(newPositions[0])
            tailPosition = list(newPositions[1])

            if tailPosition not in uniqueTailPositions:
                uniqueTailPositions.append(tailPosition)
    
    return len(uniqueTailPositions)


print(getUniqueTailPositions(input))