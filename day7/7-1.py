from input import input
    
class File:
    def __init__(self, name:str, size:int) -> None:
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name:str, parent=None) -> None:
        self.name = name
        self.files = []
        self.directories = []
        self.parent = parent

    def getDirectory(self, name:str):
        for directory in self.directories:
            if directory.name == name:
                return directory
    
    def getSize(self) -> int:
        size = 0

        for file in self.files:
            size += file.size

        for childDirectory in self.directories:
            size += childDirectory.getSize()

        return size
    
    def addFile(self, name:str, size:int) -> None:
        self.files.append(File(name, size))
    
    def addDirectory(self, name:str) -> None:
        self.directories.append(Directory(name, self))


def getMainDirectory(input:str) -> Directory:

    mainDirectory = Directory("/")
    currentDirectory = mainDirectory

    for line in input.splitlines():

        if line == "$ cd /":
            continue

        line = line.split(" ")

        if line[0] == "dir":
            currentDirectory.addDirectory(line[1])
        
        if line[0].isdigit():
            currentDirectory.addFile(line[1], int(line[0]))

        if len(line) > 2 and line[2] == "..":
            currentDirectory = currentDirectory.parent

        if line[0] == "$" and line[1] == "cd" and line[2] != "..":
            currentDirectory = currentDirectory.getDirectory(line[2])
    
    return mainDirectory

def getPuzzleAnswer(directory:Directory) -> int:
    puzzleAnswer = 0

    for childDirectory in directory.directories:
        puzzleAnswer += getPuzzleAnswer(childDirectory)

    directorySize = directory.getSize()
    if directorySize <= 100000:
        puzzleAnswer += directorySize

    return puzzleAnswer

print(getPuzzleAnswer(getMainDirectory(input)))