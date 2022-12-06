from input import input

def getStacks(input: str) -> list:
    stackIndex = []

    for line in input.splitlines():

        if line[1] == "1":
            loopCount = 0

            for char in line:
                if char != " ":
                    stackIndex.append(int(loopCount))
                loopCount += 1
            break
    
    stacks = []
    for index in stackIndex:
        stacks.append([])

    for line in input.splitlines():
        if line[1] == "1":
            break
        loopCount = 0
        for index in stackIndex:
            box = line[index]
            if box != " ":
                stacks[loopCount].insert(0, box)
            loopCount += 1
    
    return stacks

def interpretInstructions(input: str) -> list:

    instructionList = []

    for instruction in input.splitlines():
        if instruction != "" and instruction[0] == "m":
            splitInstruction = instruction.split(" ")
            instructionList.append({
                "amount": int(splitInstruction[1]),
                "from": int(splitInstruction[3]),
                "to": int(splitInstruction[5])
            })
    
    return instructionList

stacks = getStacks(input)
instructions = interpretInstructions(input)