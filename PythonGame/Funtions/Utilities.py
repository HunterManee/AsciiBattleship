from Funtions import Display

#Gets a list from the str range format
def getRangeList(rangeInput):
    coordinates = rangeInput.split(':')
    letter1 = coordinates[0][0]
    letter2 = coordinates[1][0]
    num1 = int(coordinates[0][1])
    num2 = int(coordinates[1][1])


    rangeList = []
    if letter1 == letter2:
        minNum = num1 if num1 < num2 else num2
        maxNum = num1 if num1 > num2 else num2

        for n in range(minNum, maxNum + 1):
            rangeList.append(letter1 + str(n))
    elif num1 == num2:
        minNum = ord(letter1) if ord(letter1) < ord(letter2) else ord(letter2)
        maxNum = ord(letter1) if ord(letter1) > ord(letter2) else ord(letter2)

        for n in range(minNum, maxNum + 1):
            rangeList.append(chr(n) + str(num1))

    return rangeList

def validateRangeFormat(rangeInput):
    if len(rangeInput) != 5:
        return 'Input must be a length of 5'
    
    if rangeInput[2] != ':':
        return "Input must be separated by ':'"

    coordinates = rangeInput.split(':')
    letter1 = coordinates[0][0]
    letter2 = coordinates[1][0]
    num1 = int(coordinates[0][1])
    num2 = int(coordinates[1][1])

    if coordinates[0] == coordinates[1]:
        return 'Coordinates must not be equal'

    if letter1 != letter2 and num1 != num2:
        return 'Must be vertical or horizontal coordinates'
    if not (65 <= ord(letter1) <= 74):
        return 'Coordinate out of range'
    if not (65 <= ord(letter2) <= 74):
        return 'Coordinate out of range'
    try:
        if not (0 <= num1 <= 9):
            return 'Coordinate out of range'
        if not (0 <= num2 <= 9):
            return 'Coordinate out of range'
    except:
        return 'Try A0:A1'

    
    return 'success'

def validateShipLength(shipLength, rangeInput):

    coordinates = rangeInput.split(':')
    letter1 = coordinates[0][0]
    letter2 = coordinates[1][0]
    num1 = int(coordinates[0][1])
    num2 = int(coordinates[1][1])

    xLength = abs(ord(letter2) - ord(letter1)) + 1
    yLength = abs(num2 - num1) + 1

    if xLength != int(shipLength) and yLength != int(shipLength):
        return False
    
    return True

def validatePlacement(shipRanges, rangeInput):
    inputRangeList = getRangeList(rangeInput)
    for shipRange in shipRanges.keys():
        shipRangeList = getRangeList(shipRange)
        for coor in inputRangeList:
            try:
                if shipRangeList.index(coor) != -1:
                    return False
            except: 
                continue
    return True

def validateCoordinateFormat(coordinate):
    if len(coordinate) != 2:
        return False
    
    letter = coordinate[0]
    number = coordinate[1]
    
    if letter.isnumeric() == True or number.isnumeric() == False:
        return False

    letterValid = 65 <= ord(letter) < 65 + Display.coorRange
    numberValid = 0 <= int(number) < Display.coorRange
    
    if letterValid and numberValid:
        return True
    return False