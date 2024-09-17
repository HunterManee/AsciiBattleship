from Funtions import Display
from Funtions import Ships
from Funtions import Utilities
from collections import namedtuple
import random

bot = namedtuple('bot', ['name', 'shipList', 'guessDict'])

guessPool = []
for num in range(0,Display.coorRange):
    for u in range(65, 65 + Display.coorRange):
        coor = chr(u) + str(num)
        guessPool.append(coor)


def createNewBot(name):
    shipList = getBotShips()
    guessDict = {}
    newBot = bot(name, shipList, guessDict)
    return newBot

def getBotShips():
    ships = []
    shipRanges = {}

    for shipLength in Ships.shipLengths.keys():
        for x in range(Ships.shipLengths[shipLength]):
            validRange = False
            while not validRange:
                letter = random.randint(65, 65 + Display.coorRange - 1)
                number = random.randint(0, 9)
                coor = chr(letter) + str(number)

                shipDirection = random.randint(0,4) #up, down, left, right

                shipRange = getExpectedShipRange(coor, shipDirection, shipLength)
                validRangeFormat = Utilities.validateRangeFormat(shipRange)
                if validRangeFormat != 'success':
                    continue

                validShipLength = Utilities.validateShipLength(shipLength, shipRange)
                if not validShipLength:
                    continue

                validShipPlacement = Utilities.validatePlacement(shipRanges, shipRange)
                if not validShipPlacement:
                    continue

                shipRanges[shipRange] = 'S'
                validRange = True

            ships.append(Ships.createNewShip(shipRange))

    return ships
               


def getExpectedShipRange(fromCoor, shipDirection, shipLength):
    unicode = ord(fromCoor[0])
    number = int(fromCoor[1])

    if shipDirection == 0:
        number -= shipLength + 1
    elif shipDirection == 1:
        number += shipLength - 1
    elif shipDirection == 2:
        unicode -= shipLength + 1
    elif shipDirection == 3:
        unicode += shipLength - 1

    letter = chr(unicode)
    toCoor = letter + str(number)
    validToCoor = Utilities.validateCoordinateFormat(toCoor)
    if validToCoor:
        shipRange = fromCoor + ':' + letter + str(number)
    else:
        shipRange = ''
    return shipRange

def getFiringCoordinate():
    firingCoordinate = calculateCoordinate()
    if guessPool.count(firingCoordinate) > 0:
        guessPool.remove(firingCoordinate)
    return firingCoordinate

attackingDictionary = {}
def calculateCoordinate():
    if len(attackingDictionary) == 0:
        randomIndex = random.randint(0, len(guessPool) - 1)
        firingCoordinate = guessPool[randomIndex]
        return firingCoordinate
    
    randomIndex = random.randint(0, len(attackingDictionary) - 1)
    values = list(attackingDictionary.values())
    firingCoordinate = values[randomIndex]

    return firingCoordinate
    

def hitShip(bot, firingCoordinate):
    unicode = ord(firingCoordinate[0])
    number = int(firingCoordinate[1])

    upCoor = chr(unicode) + str(number - 1)
    downCoor = chr(unicode) + str(number + 1)
    leftCoor = chr(unicode - 1) + str(number)
    rightCoor = chr(unicode + 1) + str(number)


    if len(attackingDictionary) == 0:
        if Utilities.validateCoordinateFormat(upCoor) and list(bot.guessDict.keys()).count(upCoor) == 0:
            attackingDictionary['up'] = upCoor
        if Utilities.validateCoordinateFormat(downCoor) and list(bot.guessDict.keys()).count(downCoor) == 0:
            attackingDictionary['down'] = downCoor
        if Utilities.validateCoordinateFormat(leftCoor) and list(bot.guessDict.keys()).count(leftCoor) == 0:
            attackingDictionary['left'] = leftCoor
        if Utilities.validateCoordinateFormat(rightCoor) and list(bot.guessDict.keys()).count(rightCoor) == 0:
            attackingDictionary['right'] = rightCoor
        return
    
    values = list(attackingDictionary.values())
    index = values.index(firingCoordinate)
    keys = list(attackingDictionary.keys())

    if keys[index] == 'up':
        attackingDictionary['up'] = upCoor
        if not Utilities.validateCoordinateFormat(attackingDictionary['up']) or list(bot.guessDict.keys()).count(upCoor) != 0:
            del attackingDictionary['up']
    if keys[index] == 'down':
        attackingDictionary['down'] = downCoor
        if not Utilities.validateCoordinateFormat(attackingDictionary['down']) or list(bot.guessDict.keys()).count(downCoor) != 0:
            del attackingDictionary['down']
    if keys[index] == 'left':
        attackingDictionary['left'] = leftCoor
        if not Utilities.validateCoordinateFormat(attackingDictionary['left']) or list(bot.guessDict.keys()).count(leftCoor) != 0:
            del attackingDictionary['left']
    if keys[index] == 'right':
        attackingDictionary['right'] = rightCoor
        if not Utilities.validateCoordinateFormat(attackingDictionary['right']) or list(bot.guessDict.keys()).count(rightCoor) != 0:
            del attackingDictionary['right']



        

def missShip(firingCoordinate):
    if len(attackingDictionary) == 0:
        return
    
    keys = list(attackingDictionary.keys())
    values = list(attackingDictionary.values())

    index =  values.index(firingCoordinate)

    del attackingDictionary[keys[index]]
    
