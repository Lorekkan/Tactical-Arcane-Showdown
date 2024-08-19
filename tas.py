import random
from tabulate import tabulate

# These are the 9 playable elements for this game. They replace rock, paper and scissors.
elements = ["Fire", "Water", "Wind", "Electric", "Nature", "Earth", "Metal", "Light", "Dark"]

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

defaultHP = 20
defaultStamina = 1
defaultMaxStamina = 4

class Player:
    def __init__(self, HP = defaultHP, stamina = defaultStamina, maxStamina = defaultMaxStamina):
        self.maxHP = HP
        self.HP = HP
        self.armor = 0
        self.maxStamina = maxStamina
        self.stamina = stamina
        self.staminaProgress = 0
        self.staminaGainSpeed = 2
        self.buffs = []
        self.debuffs = []
        self.matchWin = 0
        self.roundWin = 0
        self.proposedElements = None
        self.chosenElement = None
        self.powerUpElements = []
        self.powerUpActivated = False

    def gainStamina(self, amount):
        self.stamina += amount

    def updateStaminaProgress(self, amount):
        self.staminaProgress += amount
        if self.staminaProgress == self.staminaGainSpeed:
            self.gainStamina(1)
            self.staminaProgress = 0
    
    def updateStaminaGainSpeed(self, amount):
        self.staminaGainSpeed += amount
        if self.staminaGainSpeed <= 0:
            self.staminaGainSpeed == 1
    
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

    def updateHP(self, amount):
        self.HP += amount

    def hasArmor(self):
        return self.armor > 0

    def updateArmor(self, amount):
        self.armor += amount

    def refreshStats(self, HP = defaultHP, stamina = defaultStamina):
        self.HP = HP
        self.armor = 0
        self.stamina = stamina
        self.staminaProgress = 0
        self.staminaGainSpeed = 2
        self.buffs = []
        self.debuffs = []
        self.proposedElements = None
        self.chosenElement = None
        self.powerUpElements = []
        self.powerUpActivated = False

    def roundEndUpdate(self):
        if self.HP > 0:
            self.roundWin += 1
        self.refreshStats()

defaultRoundsToWin = 2

class Match:
    def __init__(self, player1, player2, roundsToWin = defaultRoundsToWin):
        self.player1 = player1
        self.player2 = player2
        self.roundsToWin = roundsToWin

    def displayGameplayScreen(self):
        # Generate values to print
        matchNumber = self.player1.matchWin + self.player2.matchWin + 1
        roundText1 = ""
        roundText2 = ""
        for i in range(self.roundsToWin):
            if i < self.player1.roundWin:
                roundText1 += " x"
            else:
                roundText1 += " \xb7"

            if i < self.player2.roundWin:
                roundText2 += " x"
            else:
                roundText2 += " \xb7"

        # Print player 1 stats
        print(f"Match {matchNumber}:")
        print("Player 1 (You):")
        print(f"Rounds:{roundText1}")
        print(f"HP: {self.player1.HP}/{self.player1.maxHP}")
        if self.player1.hasArmor():
            print(f"Armor: {self.player1.armor}")
        # Add buffs and debuffs here
        print(f"Stamina: {self.player1.stamina}/{self.player1.maxStamina}")

        # Print a seperator for better display
        print("------------------------------------------------------------")

        # Print player 2 stats
        print("Player 2 (Computer):")
        print(f"Rounds:{roundText2}")
        print(f"HP: {self.player2.HP}/{self.player2.maxHP}")
        if self.player2.hasArmor():
            print(f"Armor: {self.player2.armor}")
        # Add buffs and debuffs here
        print(f"Stamina: {self.player2.stamina}/{self.player2.maxStamina}")

    def displayWinningOdds(self):
        # Get proposed elements
        playerHeaders = self.player1.proposedElements
        compHeaders = self.player2.proposedElements

        # Get indices from the elements list
        p0 = elements.index(playerHeaders[0])
        p1 = elements.index(playerHeaders[1])
        p2 = elements.index(playerHeaders[2])
        c0 = elements.index(compHeaders[0])
        c1 = elements.index(compHeaders[1])
        c2 = elements.index(compHeaders[2])

        # Get odds from the points table list
        odds = [
            [pointTable[9*p0 + c0], pointTable[9*p0 + c1], pointTable[9*p0 + c2]],
            [pointTable[9*p1 + c0], pointTable[9*p1 + c1], pointTable[9*p1 + c2]],
            [pointTable[9*p2 + c0], pointTable[9*p2 + c1], pointTable[9*p2 + c2]]
        ]
        print(tabulate(odds, headers=compHeaders, showindex=playerHeaders, tablefmt="pretty"))

        # Display a list of powerups

    def resolvePowerUps(self):
        pass

    def resolveHPChanges(self):
        p1Index = elements.index(self.player1.chosenElement)
        p2Index = elements.index(self.player2.chosenElement)
        point = pointTable[9*p1Index + p2Index]
        self.resolvePowerUps()
        if point == 0:
            pass
        elif point > 0:
            self.player2.updateHP(-point)
        else:
            self.player1.updateHP(point)

    def updateStaminaProgress(self):
        self.player1.updateStaminaProgress(1)
        self.player2.updateStaminaProgress(1)

    def roundEndUpdate(self):
        self.player1.roundEndUpdate()
        self.player2.roundEndUpdate()
        round1 = self.player1.roundWin
        round2 = self.player2.roundWin
        if round1 == self.roundsToWin:
            self.player1.matchWin += 1
            self.player1.roundWin = 0
            self.player2.roundWin = 0
            print("You have won the match. Congratulations!")
            return True
        elif round2 == self.roundsToWin:
            self.player2.matchWin += 1
            self.player1.roundWin = 0
            self.player2.roundWin = 0
            print("I won. I proved machines are superior to humans.")
            return True
        return False

def tacticalArcaneShowdown():
    # Initialize players and game session
    player = Player()
    computer = Player()
    game = Match(player, computer)

    playerContinue = True
    computerContinue = True
    matchEnded = False

    # Game continues until both sides leave
    while playerContinue and computerContinue:
        while not matchEnded:
            game.displayGameplayScreen()

            # Print a seperator for better display
            print("------------------------------------------------------------")

            # Get 3 elements from the player
            print("Select 3 elements. Write their full names. Press Enter after each element.")
            print("Selectable Elements:")
            for el in elements:
                print(el)
            el1 = input("Enter first element: ").capitalize()
            while el1 not in elements:
                print("Your input is invalid. Please enter a valid element.")
                el1 = input("Enter first element: ").capitalize()
            el2 = input("Enter second element: ").capitalize()
            while el2 not in elements or el2 == el1:
                print("Your input is invalid. Please enter a valid element.")
                el2 = input("Enter first element: ").capitalize()
            el3 = input("Enter third element: ").capitalize()
            while el3 not in elements or el3 == el2 or el3 == el1:
                print("Your input is invalid. Please enter a valid element.")
                el3 = input("Enter third element: ").capitalize()
            player.proposeThreeElements(el1, el2, el3)

            # Get 3 elements from the computer
            compElements = random.sample(elements, 3)
            computer.proposeThreeElements(compElements[0], compElements[1], compElements[2])

            # Print an empty line for better display
            print()

            # Display winning odds to the player
            game.displayWinningOdds()

            # Print an empty line for better display
            print()

            # Player selects an element out of 3
            pFinal = input(f"Please select an element from your proposed elements {player.proposedElements}: ").capitalize()
            while pFinal not in player.proposedElements:
                print("Your input is invalid. Please enter a valid element.")
                pFinal = input(f"Please select an element from your proposed elements {player.proposedElements}: ").capitalize()
            player.chooseFinalElement(pFinal)

            # Computer selects an element out of 3
            cFinal = random.choice(computer.proposedElements)
            computer.chooseFinalElement(cFinal)

            # Winner deals damage to the loser
            game.resolveHPChanges()

            # At turn end update stamina progress for each player
            game.updateStaminaProgress()

            # Round end conditions
            if player.HP <= 0 or computer.HP <= 0:
                matchEnded = game.roundEndUpdate()

        # Ask if the player wants to continue
        reply = input("Do you want to continue? Answer with yes or no: ").lower()
        print(reply)
        while True:
            if reply == "yes":
                playerContinue = True
                break
            elif reply == "no":
                playerContinue = False
                break
            else:
                print("You have entered an invalid response. Please try again.")
                reply = input("Do you want to continue? Answer with yes or no: ").lower()
        
        # Randomly determine if the computer wants to continue
        computerContinue = random.choice([True, False])

        # Determine whether the game continues
        if playerContinue and computerContinue:
            print("Let's play another game.")
            matchEnded = False
        elif playerContinue:
            print("Sorry I have to run away.")
        elif computerContinue:
            print("I wanted to play more. What a shame.")
        else:
            print("I guess none of us wants to continue.")


tacticalArcaneShowdown()