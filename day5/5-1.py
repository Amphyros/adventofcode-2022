from inputInterpreter import stacks
from inputInterpreter import instructions

def executeInstructions(instructions: list) -> None:
    global stacks
    
    for instruction in instructions:
        for loopCount in range(0, instruction["amount"]):
            fromStack = instruction["from"] - 1
            toStack = instruction["to"] - 1
            
            moveable = stacks[fromStack][ -1 ]

            stacks[fromStack].pop(-1)
            stacks[toStack].append(moveable)

def getCrateMessage() -> str:
    global stacks
    crateMessage = ""

    for stack in stacks:
        crateMessage += stack[-1]
    
    return crateMessage


executeInstructions(instructions)
print(getCrateMessage())