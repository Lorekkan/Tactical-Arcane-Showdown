# These are the 9 playable elements for this game. They replace rock, paper and scissors.
elements = ["fire", "water", "wind", "electric", "nature", "earth", "metal", "light", "dark"]

# A 1D list for keeping the points between each element
# Suppose i and j are indices of 2 elements from the elements list:
# pointTable[9*i + j] retrieves how many points i will get against j.
pointTable = (0, -5, -2, 1, 5, -3, 3, -1, 2,
              5, 0, -1, -4, -5, 3, 2, 2, -2,
              2, 1, 0, 5, -1, -3, -5, 3, -2,
              -1, 4, -5, 0, 2, -5, 5, -3, 3,
              -5, 5, 1, -2, 0, 4, -3, 4, -4,
              3, -3, 3, 5, -4, 0, -2, 2, -4,
              -3, -2, 5, -5, 3, 2, 0, -2, 2,
              1, -2, -3, 3, -4, -2, 2, 0, 5,
              -2, 2, 2, -3, 4, 4, -2, -5, 0)

defaultHP = 15
defaultStamina = 1

class Player():
    def __init__(self, HP = defaultHP, stamina = defaultStamina):
        self.HP = HP
        self.armor = 0
        self.stamina = stamina
        self.matchWin = 0
        self.roundWin = 0
        self.proposedElements = None
        self.chosenElement = None
        self.powerUpElements = []
        self.powerUpActivated = False

    def gainStamina(self, amount):
        self.stamina += amount

    def updateRoundWin(self, match):
        self.roundWin += 1
        if (self.roundWin == match.roundsToWin):
            self.matchWin += 1
            match.player1.roundWin = 0
            match.player2.roundWin = 0
    
    def proposeThreeElements(self, el1, el2, el3):
        self.proposedElements = (el1, el2, el3)

    def activatePowerUp(self):
        if self.stamina > 0:
            self.powerUpActivated = True
            stamina -= 1
        else:
            self.powerUpActivated = False
            print("You don't have any stamina left.")

    def chooseFinalElement(self, el):
        self.chosenElement = el
        index = self.proposedElements.index(el)
        for i in range(3):
            if i == index:
                pass
            else:
                self.powerUpElements.append(self.proposedElements[i])

    def updateHealth(self, amount):
        self.HP += amount

    def updateArmor(self, amount):
        self.armor += amount

    def refreshStats(self, HP = defaultHP, stamina = defaultStamina):
        self.HP = HP
        self.armor = 0
        self.stamina = stamina
        self.proposedElements = None
        self.chosenElement = None
        self.powerUpElements = []
        self.powerUpActivated = False

defaultRoundsToWin = 2

class Match():
    def __init__(self, player1, player2, roundsToWin = defaultRoundsToWin):
        self.player1 = player1
        self.player2 = player2
        self.roundsToWin = roundsToWin


def tacticalArcaneShowdown():
    pass

def gameStartPrep():
    pass

def roundUpdate():
    pass

def matchUpdate():
    pass

def displayWinningOdds():
    pass