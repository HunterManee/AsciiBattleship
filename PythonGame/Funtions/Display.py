import os
from Funtions import Utilities


coorRange = 10

coordinatePlane = {}
for y in range(coorRange):
    for x in range(65, 65 + coorRange):
        coor = chr(x) + str(y)
        
        coordinatePlane[coor] = ' '

#### Funtions ######################################################################

def clearDisplay():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def printToTerminal(coorDict = None):
    clearDisplay()

    Display = ('   | A | B | C | D | E | F | G | H | I | J |\n'
               '-------------------------------------------\n'
               ' 0 | $ | $ | $ | $ | $ | $ | $ | $ | $ | $ |\n'
               '-------------------------------------------\n'
               ' 1 | $ | $ | $ | $ | $ | $ | $ | $ | $ | $ |\n'
               '-------------------------------------------\n'
               ' 2 | $ | $ | $ | $ | $ | $ | $ | $ | $ | $ |\n'
               '-------------------------------------------\n'
               ' 3 | $ | $ | $ | $ | $ | $ | $ | $ | $ | $ |\n'
               '-------------------------------------------\n'
               ' 4 | $ | $ | $ | $ | $ | $ | $ | $ | $ | $ |\n'
               '-------------------------------------------\n'
               ' 5 | $ | $ | $ | $ | $ | $ | $ | $ | $ | $ |\n'
               '-------------------------------------------\n'
               ' 6 | $ | $ | $ | $ | $ | $ | $ | $ | $ | $ |\n'
               '-------------------------------------------\n'
               ' 7 | $ | $ | $ | $ | $ | $ | $ | $ | $ | $ |\n'
               '-------------------------------------------\n'
               ' 8 | $ | $ | $ | $ | $ | $ | $ | $ | $ | $ |\n'
               '-------------------------------------------\n'
               ' 9 | $ | $ | $ | $ | $ | $ | $ | $ | $ | $ |\n'
               '-------------------------------------------')


    for row in range(coorRange):
        for col in range(65, 65+coorRange):
            coor = chr(col) + str(row)
            i = Display.index('$')

            strLeft = Display[:i]
            strRight = Display[i+1:]
            char = getCharFromCoorList(coor, coorDict)
            Display = strLeft + char + strRight
    
    print(Display)

def getCharFromCoorList(searchCoordinate, coordinateDictionary):
    
    if coordinateDictionary == None or len(coordinateDictionary) == 0:
        return coordinatePlane[searchCoordinate]

    for coorKey in coordinateDictionary.keys():
        if len(coorKey) == 2 and searchCoordinate == coorKey:
            return coordinateDictionary[coorKey]
        elif len(coorKey) == 5:
            rangeList = Utilities.getRangeList(coorKey)
            try:
                if rangeList.index(searchCoordinate) != -1:
                    return coordinateDictionary[coorKey]
            except:
                continue

    return coordinatePlane[searchCoordinate]
    


        
        