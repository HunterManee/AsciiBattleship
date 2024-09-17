from collections import namedtuple
from Funtions import Utilities

# length: quantitiy
shipLengths = {
    2: 4,
    3: 3,
    4: 2,
    6: 1
}


Ship = namedtuple('Ship', ['positionMap'])

def getMatchPoint():
    matchPoint = 0
    for len in shipLengths.keys():
        matchPoint += len * shipLengths[len]
    return matchPoint

def createNewShip(strRange):
    positionMap = {}
    for coor in Utilities.getRangeList(strRange):
        positionMap[coor] = 'S'
    ship = Ship(positionMap)
    return ship

def fireMissle(inTurn, attackingCoor, opponent):
    for ship in opponent.shipList:
        positionMap = ship.positionMap
        shipCoordinates = list(positionMap.keys())

        if shipCoordinates.count(attackingCoor) == 1:
            if positionMap[attackingCoor] == 'X':
                return False

            inTurn.guessDict[attackingCoor] = 'X'
            positionMap[attackingCoor] = 'X'
                        
            return True
        else:
            inTurn.guessDict[attackingCoor] = 'O'
            continue

    return False

def convertShipsIntoDictionary(shipList):
    shipDict = {}
    for ship in shipList:
        positionMap = ship.positionMap
        for key in positionMap.keys():
            shipDict[key] = positionMap[key]

    return shipDict

