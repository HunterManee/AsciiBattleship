from Funtions import Display
from Funtions import Ships
from Funtions import Utilities

from collections import namedtuple

player = namedtuple('player',['name', 'shipList', 'guessDict'])

def createNewPlayer(name):
    ships = getPlayerShips()
    guessDict = {}
    newPlayer = player(name, ships, guessDict)
    return newPlayer

def getPlayerShips():
    ships = []
    shipRanges = {}
    Display.printToTerminal()
    for shipLength in Ships.shipLengths.keys():
        for x in range(Ships.shipLengths[shipLength]):
            validRange = False
            while not validRange:
                rangeInput = input(f'Enter range for {shipLength} length ship (A0:A{shipLength - 1}):\n').upper()

                validRangeFormat = Utilities.validateRangeFormat(rangeInput)
                if validRangeFormat != 'success':
                    Display.printToTerminal(shipRanges)
                    print(f'Invalid Format: {validRangeFormat}')
                    continue

                validShipRange = Utilities.validateShipLength(shipLength, rangeInput)
                if not validShipRange:
                    Display.printToTerminal(shipRanges)
                    print(f'Invalid Length: try A0:A{shipLength - 1}')
                    continue

                validShipPlacement = Utilities.validatePlacement(shipRanges, rangeInput)
                if not validShipPlacement:
                    Display.printToTerminal(shipRanges)
                    print(f'Invalid Placement: Cannot overlap ship placements')
                    continue

                shipRanges[rangeInput] = 'S'
                validRange = True

            Display.printToTerminal(shipRanges)
            ships.append(Ships.createNewShip(rangeInput))

    return ships


