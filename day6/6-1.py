from input import input

def getStartOfPacketMarkerValue():
    loopCount = 0
    marker = ""
    
    for char in input:
        if char in marker:
            position = marker.find(char) + 1
            marker = marker[position:]

        marker += char
        loopCount += 1

        if len(marker) >= 4:
            return loopCount

print(getStartOfPacketMarkerValue())