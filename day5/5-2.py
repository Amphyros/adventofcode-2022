from inputInterpreter import stacks
from inputInterpreter import instructions

def executeInstructions(instructions: list) -> None:
    global stacks
    
    for instruction in instructions:
        fromStack = instruction["from"] - 1
        toStack = instruction["to"] - 1
            
        moveables = stacks[fromStack][ -instruction["amount"]: ]

        removalIndex = len(moveables)
        for moveable in moveables:
            stacks[fromStack].pop(-removalIndex)
            stacks[toStack].append(moveable)
            removalIndex -= 1
        

def getCrateMessage() -> str:
    global stacks
    crateMessage = ""

    for stack in stacks:
        crateMessage += stack[-1]
    
    return crateMessage


executeInstructions(instructions)
print(getCrateMessage())