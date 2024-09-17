from Funtions import Players
from Funtions import Bots
from Funtions import Display
from Funtions import Ships

from Funtions import Utilities

import random

inMatch = True
matchPoint = Ships.getMatchPoint()

playerHitCounter = 0
botHitCounter = 0

Display.clearDisplay()

userName = input('Enter your name to begin >> ')
Player = Players.createNewPlayer(userName)
input('press Enter to continue...')

Bot = Bots.createNewBot('Terminator')

playerList = [Player, Bot]
turnCounter = random.randint(0,1)
validCoordinate = True
while inMatch:
    inTurn = playerList[turnCounter % 2]
    oppenent = playerList[0] if inTurn.name != playerList[0].name else playerList[1]

    Display.printToTerminal(inTurn.guessDict)
    if not validCoordinate:
        print('Trajectory out of range')

    firingCoordinate = input('Firing coordinate A0: ').upper() if inTurn.name != 'Terminator' else Bots.getFiringCoordinate()
    validCoordinate = Utilities.validateCoordinateFormat(firingCoordinate)
    if not validCoordinate:
        continue

    contact = Ships.fireMissle(inTurn, firingCoordinate, oppenent)

    playerHitCounter += 1 if inTurn.name == 'Terminator' and contact else 0
    botHitCounter += 1 if inTurn.name != 'Terminator' and contact else 0

    if inTurn.name == 'Terminator':
        if contact:
            Bots.hitShip(inTurn, firingCoordinate)
        elif not contact:
            Bots.missShip(firingCoordinate)

        shipDict = Ships.convertShipsIntoDictionary(oppenent.shipList)
        Display.printToTerminal(shipDict)
    else:
        Display.printToTerminal(inTurn.guessDict)
    input('press Enter to continue...')

    turnCounter += 1

    if playerHitCounter == matchPoint or botHitCounter == matchPoint:
        inMatch = False

