import random
from tabulate import tabulate

# These are the 9 playable elements for this game. They replace rock, paper and scissors.
elements = ["Fire", "Water", "Wind", "Electric", "Nature", "Earth", "Metal", "Light", "Dark"]

# A 1D list for keeping the points between each element
# Suppose i and j are indices of 2 elements from the elements list:
# pointTable[9*i + j] retrieves how many points i will get against j.
pointTable = [0, -5, -2, 1, 5, -3, 3, -1, 2,
              5, 0, -1, -4, -5, 3, 2, 2, -2,
              2, 1, 0, 5, -1, -3, -5, 3, -2,
              -1, 4, -5, 0, 2, -5, 5, -3, 3,
              -5, 5, 1, -2, 0, 4, -3, 4, -4,
              3, -3, 3, 5, -4, 0, -2, 2, -4,
              -3, -2, 5, -5, 3, 2, 0, -2, 2,
              1, -2, -3, 3, -4, -2, 2, 0, 5,
              -2, 2, 2, -3, 4, 4, -2, -5, 0]

# Default values for games
defaultHP = 20
defaultStamina = 1
defaultMaxStamina = 5

# Player object
class Player:
    def __init__(self, HP = defaultHP, stamina = defaultStamina, maxStamina = defaultMaxStamina):
        self.maxHP = HP
        self.HP = HP
        self.armor = 0
        self.maxStamina = maxStamina
        self.stamina = stamina
        self.staminaProg = 0
        self.brilliance = 2
        self.buffs = []
        self.debuffs = []
        self.matchWin = 0
        self.roundWin = 0
        self.proposedElements = None
        self.chosenElement = None
        self.powerUpElements = []
        self.powerUpActivated = False
        self.lockedElements = []
        self.sunshine = False
        self.rejuvinating = False
        self.armorDamage = 0
        self.usedElements = []
        self.dmgMultiplier = 1
        self.cavalry = False
        self.darkKnight = False

    # Increases stamina of the player
    def gainStamina(self, amount):
        if self.stamina < self.maxStamina:
            self.stamina += amount

    # At the end of each turn the player makes stamina gain progress
    def updatestaminaProg(self, amount):
        self.staminaProg += amount
        if self.staminaProg == self.brilliance:
            self.gainStamina(1)
            self.staminaProg = 0
    
    # Changes how many turns are needed to earn stamina
    def updateBrilliance(self, amount):
        self.brilliance += amount
        if self.brilliance <= 0:
            self.brilliance == 1
    
    def proposeThreeElements(self, el1, el2, el3):
        self.proposedElements = [el1, el2, el3]

    def activatePowerUp(self):
        if self.stamina > 0:
            self.powerUpActivated = True
            self.stamina -= 1
            # Add power up to used elements
            for el in self.powerUpElements:
                if el not in self.usedElements:
                    self.usedElements.append(el)
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
        
        # Add chosen element to used elements
        if el not in self.usedElements:
            self.usedElements.append(el)

    def updateHP(self, amount):
        if self.HP < self.maxHP:
            self.HP += amount

    def hasArmor(self):
        return self.armor > 0

    def updateArmor(self, amount):
        self.armor += amount
        if self.armor < 0:
            remDamage = -self.armor
            self.armor = 0
            return remDamage
        return 0

    # After round and match ends refresh each players stats
    def refreshStats(self, HP = defaultHP, stamina = defaultStamina):
        self.HP = HP
        self.armor = 0
        self.stamina = stamina
        self.staminaProg = 0
        self.brilliance = 2
        self.buffs = []
        self.debuffs = []
        self.proposedElements = None
        self.chosenElement = None
        self.powerUpElements = []
        self.powerUpActivated = False
        self.lockedElements = []
        self.sunshine = False
        self.rejuvinating = False
        self.armorDamage = 0
        self.usedElements = []
        self.dmgMultiplier = 1
        self.cavalry = False
        self.darkKnight = False

defaultRoundsToWin = 2

class Match:
    def __init__(self, player1, player2, roundsToWin = defaultRoundsToWin):
        self.player1 = player1
        self.player2 = player2
        self.roundsToWin = roundsToWin
        self.meteorCount = 0
        self.whirlpool = False
        self.locked = None
        self.rainbow = False
        self.reverse = False
        self.zathura = 0
        self.powerBlock = False

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
        if self.player1.buffs:
            print(f"Buffs: {self.player1.buffs}")
        if self.player1.debuffs:
            print(f"Debuffs: {self.player1.debuffs}")
        print(f"Stamina: {self.player1.stamina}/{self.player1.maxStamina}")

        # Print a seperator for better display
        print("------------------------------------------------------------")

        # Print player 2 stats
        print("Player 2 (Computer):")
        print(f"Rounds:{roundText2}")
        print(f"HP: {self.player2.HP}/{self.player2.maxHP}")
        if self.player2.hasArmor():
            print(f"Armor: {self.player2.armor}")
        if self.player2.buffs:
            print(f"Buffs: {self.player2.buffs}")
        if self.player2.debuffs:
            print(f"Debuffs: {self.player2.debuffs}")
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

    def resolvePowerUps(self, point):
        # Player 2 light-dark and fire-electric power ups are performed seperately at the start
        # because they might effect other player 1 power ups
        if self.player2.powerUpActivated:
            if "Fire" in self.player2.powerUpElements and "Electric" in self.player2.powerUpElements:
                print("Computer activated Chip Malfunction.")
                for i in range(81):
                    pointTable[i] *= -1
            elif "Light" in self.player2.powerUpElements and "Dark" in self.player2.powerUpElements:
                print("Computer activated Yin and Yang")
                point *= -1
        if self.player1.powerUpActivated:
            powerUp = self.player1.powerUpElements
            # What each power up does is explained in README file
            if "Fire" in powerUp and "Water" in powerUp:
                print("You activated Boiling Point.")
                if "Boiling" not in self.player2.debuffs:
                    self.player2.debuffs.append("Boiling")
            elif "Fire" in powerUp and "Wind" in powerUp:
                print("You activated Drought.")
                self.player2.buffs = []
            elif "Fire" in powerUp and "Nature" in powerUp:
                print("You activated Forest Fire.")
                for i in range(self.player1.buffs.count("Stack+")):
                    self.player2.debuffs.append("Burn")
            elif "Fire" in powerUp and "Electric" in powerUp:
                print("You activated Chip Malfunction.")
                for i in range(81):
                    pointTable[i] *= -1
            elif "Fire" in powerUp and "Earth" in powerUp:
                print("You activated Meteor Strike.")
                self.meteorCount += 1
            elif "Fire" in powerUp and "Metal" in powerUp:
                print("You activated Hephaestus to the Rescue.")
                for i in range(self.player1.buffs.count("Stack+")):
                    self.player1.buffs.append("Forge")
            elif "Fire" in powerUp and "Light" in powerUp:
                print("You activated Sun Will Shine On Us Again.")
                self.player1.buffs.append("Sunshine")
                self.player1.sunshine = True
            elif "Fire" in powerUp and "Dark" in powerUp:
                print("You activated Cauldron Upgrade.")
                self.player1.buffs.append("Dot")
            elif "Water" in powerUp and "Wind" in powerUp:
                print("You activated Whirlpool.")
                self.whirlpool = not self.whirlpool
            elif "Water" in powerUp and "Nature" in powerUp:
                print("You activated Rejuvinating Waters.")
                self.player1.rejuvinating = True
            elif "Water" in powerUp and "Electric" in powerUp:
                print("You activated Thrown Into an Electric Eel Tank.")
                for i in range(self.player1.buffs.count("Stack+")):
                    self.player2.debuffs.append("Shock")
            elif "Water" in powerUp and "Earth" in powerUp:
                print("You activated Stuck in the Swamp.")
                if point > 0:
                    self.player2.updateBrilliance(1)
                elif point < 0:
                    self.player1.updateBrilliance(1)
            elif "Water" in powerUp and "Metal" in powerUp:
                print("You activated Shields Are Failing.")
                if point > 0:
                    self.player2.armorDamage = self.player2.armor
                    self.player2.armor = 0
                elif point < 0:
                    self.player1.armorDamage = self.player2.armor
            elif "Water" in powerUp and "Light" in powerUp:
                print("You activated The Dark Side of the Moon.")
                self.rainbow = not self.rainbow
            elif "Water" in powerUp and "Dark" in powerUp:
                print("You activated Bermuda Triangle.")
                if "Lost" not in self.player2.debuffs:
                    self.player2.debuffs.append("Lost")
            elif "Wind" in powerUp and "Nature" in powerUp:
                print("You activated What Goes Around, Comes Around.")
                self.reverse = not self.reverse
            elif "Wind" in powerUp and "Electric" in powerUp:
                print("You activated You Are Not Worthy.")
                self.player1.buffs.append("Stack+")
            elif "Wind" in powerUp and "Earth" in powerUp:
                print("You activated Sandstorm.")
                for i in range(self.player1.buffs.count("Stack+")):
                    self.player2.debuffs.append("Dust")
            elif "Wind" in powerUp and "Metal" in powerUp:
                print("You activated Industial Revolution.")
                if point > 0:
                    self.player1.updateBrilliance(-1)
                    if self.player1.staminaProg == self.player1.brilliance:
                        self.player1.gainStamina(1)
                        self.player1.staminaProg = 0
                elif point < 0:
                    self.player1.updateBrilliance(1)
            elif "Wind" in powerUp and "Light" in powerUp:
                print("You activated Summer Breeze.")
                self.player1.debuffs = []
            elif "Wind" in powerUp and "Dark" in powerUp:
                print("You activated Zathura.")
                self.zathura += 1
            elif "Nature" in powerUp and "Electric" in powerUp:
                print("You activated Spoiled Plants.")
                self.player2.debuffs.append("Poisoned")
                for i in range(self.player1.buffs.count("Stack+")):
                    self.player2.debuffs.append("Poisoned")
            elif "Nature" in powerUp and "Earth" in powerUp:
                print("You activated Regenerative Tissue.")
                for i in range(self.player1.buffs.count("Stack+")):
                    self.player1.buffs.append("Herb")
            elif "Nature" in powerUp and "Metal" in powerUp:
                print("You activated Harvest the Crops.")
                if point > 0:
                    self.player2.armorDamage = self.player1.armor
                elif point < 0:
                    self.player1.armor = 0
            elif "Nature" in powerUp and "Light" in powerUp:
                print("You activated Overgrowing Snapvine.")
                if "Trapped" not in self.player2.debuffs:
                    self.player2.debuffs.append("Trapped")
            elif "Nature" in powerUp and "Dark" in powerUp:
                print("You activated Mind Swap.")
                if point > 0 and self.player1.HP < self.player2.HP or point < 0 and self.player1.HP > self.player2.HP:
                    self.player1.HP, self.player2.HP = self.player2.HP, self.player1.HP
                    self.player1.armor, self.player2.armor = self.player2.armor, self.player1.armor
                    self.player1.stamina, self.player2.stamina = self.player2.stamina, self.player1.stamina
                    self.player1.staminaProg, self.player2.staminaProg = self.player2.staminaProg, self.player1.staminaProg
                    self.player1.brilliance, self.player2.brilliance = self.player2.brilliance, self.player1.brilliance
            elif "Electric" in powerUp and "Earth" in powerUp:
                print("You activated Hold Any Charges.")
                if self.player2.powerUpActivated:
                    if "Electric" in self.player2.powerUpElements and "Earth" in self.player2.powerUpElements:
                        self.player1.debuffs, self.player2.debuffs = self.player2.debuffs, self.player1.debuffs
                    else:
                        self.player2.debuffs += self.player1.debuffs
                        self.player1.debuffs = []
            elif "Electric" in powerUp and "Metal" in powerUp:
                print("You activated Let Him Cook.")
                if point > 0:
                    if self.player2.armor:
                        self.player2.dmgMultiplier = 3
                    else:
                        self.player2.dmgMultiplier = 2
                elif point < 0:
                    if self.player1.armor:
                        self.player1.dmgMultiplier = 3
                    else:
                        self.player1.dmgMultiplier = 2
            elif "Electric" in powerUp and "Light" in powerUp:
                print("You activated Daylight Saving Time.")
                if point < 0:
                    self.player1.gainStamina(3)
            elif "Electric" in powerUp and "Dark" in powerUp:
                print("You activated Back to the Dark Ages.")
                if point > 0:
                    self.powerBlock = True
                elif point < 0:
                    self.player1.stamina = 0
                    self.player1.staminaProg = 0
            elif "Earth" in powerUp and "Metal" in powerUp:
                print("You activated Greatest Earth Bender.")
                if point < 0:
                    self.player1.dmgMultiplier = 0
                elif point > 0:
                    self.player1.dmgMultiplier = 0.5
            elif "Earth" in powerUp and "Light" in powerUp:
                print("You activated Come Get Your Armor.")
                for i in range(self.player1.buffs.count("Stack+")):
                    self.player1.buffs.append("Tough")
            elif "Earth" in powerUp and "Dark" in powerUp:
                print("You activated SMASH!.")
                for i in range(self.player1.buffs.count("Stack+")):
                    self.player2.debuffs.append("Quake")
            elif "Metal" in powerUp and "Light" in powerUp:
                print("You activated The Cavalry is Here.")
                self.player1.cavalry = True
            elif "Metal" in powerUp and "Dark" in powerUp:
                print("You activated The Dark Knight Rises.")
                self.player1.darkKnight = True
            elif "Light" in powerUp and "Dark" in powerUp:
                print("You activated Yin and Yang.")
                point *= -1
        if self.player2.powerUpActivated:
            powerUp = self.player2.powerUpElements
            if "Fire" in powerUp and "Water" in powerUp:
                print("Computer activated Boiling Point.")
                if "Boiling" not in self.player1.debuffs:
                    self.player1.debuffs.append("Boiling")
            elif "Fire" in powerUp and "Wind" in powerUp:
                print("Computer activated Drought.")
                self.player1.buffs = []
            elif "Fire" in powerUp and "Nature" in powerUp:
                print("Computer activated Forest Fire.")
                for i in range(self.player2.buffs.count("Stack+")):
                    self.player1.debuffs.append("Burn")
            elif "Fire" in powerUp and "Earth" in powerUp:
                print("Computer activated Meteor Strike.")
                self.meteorCount += 1
            elif "Fire" in powerUp and "Metal" in powerUp:
                print("Computer activated Hephaestus to the Rescue.")
                for i in range(self.player2.buffs.count("Stack+")):
                    self.player2.buffs.append("Forge")
            elif "Fire" in powerUp and "Light" in powerUp:
                print("Computer activated Sun Will Shine On Us Again.")
                self.player2.buffs.append("Sunshine")
                self.player2.sunshine = True
            elif "Fire" in powerUp and "Dark" in powerUp:
                print("Computer activated Cauldron Upgrade.")
                self.player2.buffs.append("Dot")
            elif "Water" in powerUp and "Wind" in powerUp:
                print("Computer activated Whirlpool.")
                self.whirlpool = not self.whirlpool
            elif "Water" in powerUp and "Nature" in powerUp:
                print("Computer activated Rejuvinating Waters.")
                self.player2.rejuvinating = True
            elif "Water" in powerUp and "Electric" in powerUp:
                print("Computer activated Thrown Into an Electric Eel Tank.")
                for i in range(self.player2.buffs.count("Stack+")):
                    self.player1.debuffs.append("Shock")
            elif "Water" in powerUp and "Earth" in powerUp:
                print("Computer activated Stuck in the Swamp.")
                if point > 0:
                    self.player2.updateBrilliance(1)
                elif point < 0:
                    self.player1.updateBrilliance(1)
            elif "Water" in powerUp and "Metal" in powerUp:
                print("Computer activated Shields are Failing.")
                if point > 0:
                    self.player2.armorDamage = self.player1.armor
                elif point < 0:
                    self.player1.armorDamage = self.player1.armor
                    self.player1.armor = 0
            elif "Water" in powerUp and "Light" in powerUp:
                print("Computer activated The Dark Side of the Moon.")
                self.rainbow = not self.rainbow
            elif "Water" in powerUp and "Dark" in powerUp:
                print("Computer activated Bermuda Triangle.")
                if "Lost" not in self.player1.debuffs:
                    self.player1.debuffs.append("Lost")
            elif "Wind" in powerUp and "Nature" in powerUp:
                print("Computer activated What Goes Around, Comes Around.")
                self.reverse = not self.reverse
            elif "Wind" in powerUp and "Electric" in powerUp:
                print("Computer activated You Are Not Worthy.")
                self.player1.buffs.append("Stack+")
            elif "Wind" in powerUp and "Earth" in powerUp:
                print("Computer activated Sandstorm.")
                for i in range(self.player1.buffs.count("Stack+")):
                    self.player2.debuffs.append("Dust")
            elif "Wind" in powerUp and "Metal" in powerUp:
                print("Computer activated Industrial Revolution.")
                if point > 0:
                    self.player2.updateBrilliance(1)
                elif point < 0:
                    self.player2.updateBrilliance(-1)
                    if self.player2.staminaProg == self.player2.brilliance:
                        self.player2.gainStamina(1)
                        self.player2.staminaProg = 0
            elif "Wind" in powerUp and "Light" in powerUp:
                print("Computer activated Summer Breeze.")
                self.player2.debuffs = []
            elif "Wind" in powerUp and "Dark" in powerUp:
                print("Computer activated Zathura.")
                self.zathura += 1
            elif "Nature" in powerUp and "Electric" in powerUp:
                print("Computer activated Spoiled Plants.")
                self.player1.debuffs.append("Poisoned")
                for i in range(self.player2.buffs.count("Stack+")):
                    self.player1.debuffs.append("Poisoned")
            elif "Nature" in powerUp and "Earth" in powerUp:
                print("Computer activated Regenerative Tissue.")
                for i in range(self.player1.buffs.count("Stack+")):
                    self.player1.buffs.append("Herb")
            elif "Nature" in powerUp and "Metal" in powerUp:
                print("Computer activated Harvest the Crops.")
                if point > 0:
                    self.player2.armor = 0
                elif point < 0:
                    self.player1.armorDamage = self.player2.armor
            elif "Nature" in powerUp and "Light" in powerUp:
                print("Computer activated Overgrowing Snapvine.")
                if "Trapped" not in self.player1.debuffs:
                    self.player1.debuffs.append("Trapped")
            elif "Nature" in powerUp and "Dark" in powerUp:
                print("Computer activated Mind Swap.")
                if point > 0 and self.player1.HP < self.player2.HP or point < 0 and self.player1.HP > self.player2.HP:
                        self.player1.HP, self.player2.HP = self.player2.HP, self.player1.HP
                        self.player1.armor, self.player2.armor = self.player2.armor, self.player1.armor
                        self.player1.stamina, self.player2.stamina = self.player2.stamina, self.player1.stamina
                        self.player1.staminaProg, self.player2.staminaProg = self.player2.staminaProg, self.player1.staminaProg
                        self.player1.brilliance, self.player2.brilliance = self.player2.brilliance, self.player1.brilliance
            elif "Electric" in powerUp and "Earth" in powerUp:
                print("Computer activated Hold Any Charges.")
                if self.player2.powerUpActivated:
                    if "Electric" not in self.player1.powerUpElements or "Earth" not in self.player1.powerUpElements:
                        self.player1.debuffs += self.player2.debuffs
                        self.player2.debuffs = []
            elif "Electric" in powerUp and "Metal" in powerUp:
                print("Computer activated Let Him Cook.")
                if point > 0:
                    if self.player2.armor:
                        self.player2.dmgMultiplier = 3
                    else:
                        self.player2.dmgMultiplier = 2
                elif point < 0:
                    if self.player1.armor:
                        self.player1.dmgMultiplier = 3
                    else:
                        self.player1.dmgMultiplier = 2
            elif "Electric" in powerUp and "Light" in powerUp:
                print("Computer activated Daylight Saving Time.")
                if point > 0:
                    self.player2.gainStamina(3)
            elif "Electric" in powerUp and "Dark" in powerUp:
                print("Computer activated Back to the Dark Ages.")
                if point > 0:
                    self.player2.stamina = 0
                    self.player2.staminaProg = 0
                elif point < 0:
                    self.powerBlock = True
            elif "Earth" in powerUp and "Metal" in powerUp:
                print("Computer activated Greatest Earth Bender.")
                if point < 0:
                    self.player1.dmgMultiplier = 0.5
                elif point > 0:
                    self.player1.dmgMultiplier = 0
            elif "Earth" in powerUp and "Light" in powerUp:
                print("Computer activated Come Get Your Armor.")
                for i in range(self.player2.buffs.count("Stack+")):
                    self.player2.buffs.append("Tough")
            elif "Earth" in powerUp and "Dark" in powerUp:
                print("Computer activated SMASH!.")
                for i in range(self.player2.buffs.count("Stack+")):
                    self.player1.debuffs.append("Quake")
            elif "Metal" in powerUp and "Light" in powerUp:
                print("Computer activated The Cavalry is Here.")
                self.player2.cavalry = True
            elif "Metal" in powerUp and "Dark" in powerUp:
                print("Computer activated The Dark Knight Rises.")
                self.player2.darkKnight = True
        self.player1.powerUpElements = []
        self.player2.powerUpElements = []
        self.player1.powerUpActivated = False
        self.player2.powerUpActivated = False

    def resolveHPChanges(self):
        player = self.player1
        computer = self.player2

        # Get element indices and damage for this turn
        p1Index = elements.index(player.chosenElement)
        p2Index = elements.index(computer.chosenElement)
        point = pointTable[9*p1Index + p2Index]

        # Nature use Burn damage
        if player.chosenElement == "Nature" or "Nature" in player.powerUpElements and player.powerUpActivated:
            burnP = player.debuffs.count("Burn")
            if burnP:
                dotC = computer.buffs.count("Dot")
                player.updateHP(-burnP * dotC)
                print(f"Burn dealt {burnP*dotC} damage to you.")

        if computer.chosenElement == "Nature" or "Nature" in computer.powerUpElements and computer.powerUpActivated:
            burnC = computer.debuffs.count("Burn")
            if burnC:
                dotP = player.buffs.count("Dot")
                computer.updateHP(-burnC * dotP)
                print(f"Burn dealt {burnC*dotP} damage to computer.")

        # Power up activation Shock damage
        if player.powerUpActivated:
            shockP = player.debuffs.count("Shock")
            if shockP:
                dotC = computer.buffs.count("Dot")
                player.updateHP(-shockP * dotC)
                print(f"Shock dealt {shockP*dotC} damage to you.")
        
        if computer.powerUpActivated:
            shockC = player.debuffs.count("Shock")
            if shockC:
                dotP = computer.buffs.count("Dot")
                computer.updateHP(-shockC * dotP)
                print(f"Shock dealt {shockC*dotP} damage to computer.")

        # Wind not activated Dust damage
        if player.chosenElement == "Wind" or "Wind" in player.powerUpElements and player.powerUpActivated:
            pass
        else:
            dustP = player.debuffs.count("Dust")
            if dustP:
                dotC = computer.buffs.count("Dot")
                player.updateHP(-dustP * dotC)
                print(f"Dust dealt {dustP*dotC} damage to you.")
        
        if computer.chosenElement == "Wind" or "Wind" in computer.powerUpElements and computer.powerUpActivated:
            pass
        else:
            dustC = player.debuffs.count("Dust")
            if dustC:
                dotC = computer.buffs.count("Dot")
                player.updateHP(-dustC * dotC)
                print(f"Dust dealt {dustC*dotC} damage to computer.")
        
        # Earth use Quake damage
        if player.chosenElement == "Earth" or "Earth" in player.powerUpElements and player.powerUpActivated:
            quakeP = player.debuffs.count("Quake")
            if quakeP:
                dotC = computer.buffs.count("Dot")
                player.updateHP(-quakeP * dotC)
                print(f"Quake dealt {quakeP*dotC} damage to you.")

        if computer.chosenElement == "Earth" or "Earth" in computer.powerUpElements and computer.powerUpActivated:
            quakeC = computer.debuffs.count("Quake")
            if quakeC:
                dotP = player.buffs.count("Dot")
                computer.updateHP(-quakeC * dotP)
                print(f"Quake dealt {quakeC*dotP} damage to computer.")
                
        if not self.powerBlock:
            self.resolvePowerUps(point)

        # Normal Damage
        if point == 0:
            pass
        elif point > 0:
            point += player.buffs.count("Forge")
            point += player.armorDamage
            if player.sunshine:
                point += 2 * player.buffs.count("Sunshine")
            point *= computer.dmgMultiplier
            point = int(point)
            if player.rejuvinating:
                heal = point
                point = int(point/2)
                player.updateHP(heal)
                print(f"You have healed {heal} HP.")
            if player.cavalry:
                player.updateArmor(point)
                print(f"You've gained {point} armor from cavalry.")
            if computer.cavalry:
                armor = int(point/2)
                computer.updateArmor(armor)
                print(f"Computer has gained {armor} armor from cavalry.")
            if player.darkKnight:
                armor = 2 * point
                point = int(point/2)
                player.updateArmor(armor)
                print(f"You've gained {armor} armor from dark knight.")
            computer.updateHP(-point)
            print(f"Player's {elements[p1Index]} dealt {point} damage to Computer's {elements[p2Index]}")
        else:
            point -= computer.buffs.count("Forge")
            point -= computer.armorDamage
            if computer.sunshine:
                point -= 2 * computer.buffs.count("Sunshine")
            point *= player.dmgMultiplier
            point = int(point)
            if computer.rejuvinating:
                heal = -point
                point = int(point/2)
                computer.updateHP(heal)
                print(f"Computer has healed {heal} HP.")
            if player.cavalry:
                armor = int(-point/2)
                player.updateArmor(armor)
                print(f"You've gained {armor} armor from cavalry.")
            if computer.cavalry:
                computer.updateArmor(-point)
                print(f"Computer has gained {-point} armor from cavalry.")
            if computer.darkKnight:
                armor = - 2 * point
                point = int(point/2)
                computer.updateArmor(armor)
                print(f"Computer has gained {armor} armor from dark knight.")
            player.updateHP(point)
            print(f"Computer's {elements[p2Index]} dealt {-point} damage to Player's {elements[p1Index]}")
        player.sunshine = False
        computer.sunshine = False
        player.rejuvinating = False
        computer.rejuvinating = False
        player.armorDamage = 0
        computer.armorDamage = 0
        player.dmgMultiplier = 1
        computer.dmgMultiplier = 1
        player.cavalry = False
        computer.cavalry = False
        player.darkKnight = False
        computer.darkKnight = False

    def updatestaminaProg(self):
        self.player1.updatestaminaProg(1)
        self.player2.updatestaminaProg(1)

    def roundEndCheck(self, condition):
        player = self.player1
        computer = self.player2

        if condition == "normal":
            playerHP = player.HP
            computerHP = computer.HP
            if playerHP and computerHP:
                return None
            elif playerHP:
                return player
            elif computerHP:
                return computer
            else:
                if playerHP > computerHP:
                    return player
                elif playerHP < computerHP:
                    return computer
                else:
                    return None
        
        elif condition == "reverse":
            playerHP = player.HP
            computerHP = computer.HP
            if playerHP and computerHP:
                return None
            elif playerHP:
                return computer
            elif computerHP:
                return player
            else:
                if playerHP > computerHP:
                    return computer
                elif playerHP < computerHP:
                    return player
                else:
                    return None
                
        elif condition == "rainbow":
            playerRainbow = len(player.usedElements)
            computerRainbow = len(computer.usedElements)
            if playerRainbow == 9 and computerRainbow == 9:
                return None
            elif playerRainbow == 9:
                return player
            elif computerRainbow == 9:
                return computer
            else:
                return None

    def roundEndUpdate(self, winner):
        winner.roundWin += 1
        self.player1.refreshStats()
        self.player2.refreshStats()
        self.meteorCount = 0
        self.whirlpool = False
        self.locked = None
        self.rainbow = False
        self.reverse = False
        self.zathura = 0
        self.powerBlock = False
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
            # Round start whirlpool lock
            if game.whirlpool:
                game.locked = random.choice(elements)
                print(f"Whirlpool locked {game.locked} this turn.")
            else:
                game.locked = None

            # Round start Lost lock
            if "Lost" in player.debuffs:
                player.lockedElements = player.proposedElements
            
            if "Lost" in computer.debuffs:
                computer.lockedElements = computer.proposedElements

            # Round start Trapped lock
            if "Trapped" in player.debuffs:
                player.lockedElements.append(player.chosenElement)

            if "Trapped" in computer.debuffs:
                computer.lockedElements.append(computer.chosenElement)
            
            if player.lockedElements:
                print(f"These elements are locked for you this turn: {player.lockedElements}")
            if computer.lockedElements:
                print(f"These elements are locked for computer this turn: {computer.lockedElements}")

            # Round start Tough armor
            armorP = player.buffs.count("Tough")
            if armorP:
                player.updateArmor(armorP)
                print(f"You have gained {armorP} armor from Tough.")

            armorC = computer.buffs.count("Tough")
            if armorC:
                computer.updateArmor(armorC)
                print(f"You have gained {armorC} armor from Tough.")

            # Round start Zathura damage
            if game.zathura:
                player.updateHP(-game.zathura)
                computer.updateHP(-game.zathura)
                print(f"Zathura has dealt {game.zathura} damage to both players.")

            # Round start Meteor damage
            for i in range(game.meteorCount):
                randPlayer = random.choice([player, computer])
                randPlayer.updateHP(-1)
                if randPlayer == player:
                    print("Meteor dealt 1 damage to you.")
                else:
                    print("Meteor dealt 1 damage to computer.")

            # Round start Burn damage
            burnP = player.debuffs.count("Burn")
            dotC = computer.buffs.count("Dot")
            if burnP:
                player.updateHP(-burnP * dotC)
                print(f"Burn dealt {burnP*dotC} damage to you.")

            burnC = computer.debuffs.count("Burn")
            dotP = player.buffs.count("Dot")
            if burnC:
                computer.updateHP(-burnC * dotP)
                print(f"Burn dealt {burnC*dotP} damage to computer.")

            # Round start Shock damage
            shockP = player.debuffs.count("Shock")
            if shockP:
                player.updateHP(-shockP * dotC)
                print(f"Shock dealt {shockP*dotC} damage to you.")

            shockC = player.debuffs.count("Shock")
            if shockC:
                computer.updateHP(-shockC * dotP)
                print(f"Shock dealt {shockC*dotP} damage to computer.")

            # Round start Dust damage
            dustP = player.debuffs.count("Dust")
            if dustP:
                player.updateHP(-dustP * dotC)
                print(f"Dust dealt {dustP*dotC} damage to you.")

            dustC = player.debuffs.count("Dust")
            if dustC:
                computer.updateHP(-dustC * dotP)
                print(f"Dust dealt {dustP*dotP} damage to computer.")

            # Round start Poisoned damage
            if "Poisoned" in player.debuffs:
                player.updateHP(-2-dotC)
                print(f"Poison dealt {2+dotC} damage to you.")
                player.debuffs.remove("Poisoned")
            
            if "Poisoned" in computer.debuffs:
                computer.updateHP(-2-dotP)
                print(f"Poison dealt {2+dotP} damage to computer.")
                computer.debuffs.remove("Poisoned")

            # Round start Quake damage
            quakeP = player.debuffs.count("Quake")
            if quakeP:
                player.updateHP(-quakeP * dotC)
                print(f"Quake dealt {quakeP*dotC} damage to you.")

            quakeC = player.debuffs.count("Quake")
            if quakeC:
                computer.updateHP(-quakeC * dotP)
                print(f"Quake dealt {quakeC*dotP} damage to computer.")
                
            # Round start Herb heal
            herbP = player.buffs.count("Herb")
            if herbP:
                player.updateHP(herbP)
            
            herbC = computer.buffs.count("Herb")
            if herbC:
                computer.updateHP(herbC)

            # Check if the round ended after HP changes
            if game.reverse:
                winner = game.roundEndCheck("reverse")
                if winner:
                    print("A player has won by depleting their HP.")
                    matchEnded = game.roundEndUpdate(winner)
                    if matchEnded:
                        break
            else:
                winner = game.roundEndCheck("normal")
                if winner:
                    print("A player has won by depleting enemy HP.")
                    matchEnded = game.roundEndUpdate(winner)
                    if matchEnded:
                        break

            game.displayGameplayScreen()

            # Print a seperator for better display
            print("------------------------------------------------------------")

            # Get 3 elements from the computer
            compSelectable = elements.copy()
            compSelectable.remove(game.locked)
            for el in computer.lockedElements:
                compSelectable.remove(el)
            compElements = random.sample(compSelectable, 3)
            computer.proposeThreeElements(compElements[0], compElements[1], compElements[2])

            if "Boiling" in computer.debuffs:
                print(f"Computer's elements are {computer.proposedElements}")

            # Get 3 elements from the player
            print("Select 3 elements. Write their full names. Press Enter after each element.")
            print("Selectable Elements:")
            playerSelectable = elements.copy()
            playerSelectable.remove(game.locked)
            for el in player.lockedElements:
                playerSelectable.remove(el)
            for el in playerSelectable:
                print(el)
            el1 = input("Enter first element: ").capitalize()
            while el1 not in playerSelectable:
                print("Your input is invalid. Please enter a valid element.")
                el1 = input("Enter first element: ").capitalize()
            el2 = input("Enter second element: ").capitalize()
            while el2 not in playerSelectable or el2 == el1:
                print("Your input is invalid. Please enter a valid element.")
                el2 = input("Enter first element: ").capitalize()
            el3 = input("Enter third element: ").capitalize()
            while el3 not in playerSelectable or el3 == el2 or el3 == el1:
                print("Your input is invalid. Please enter a valid element.")
                el3 = input("Enter third element: ").capitalize()
            player.proposeThreeElements(el1, el2, el3)

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

            # Check rainbow round end condition
            if game.rainbow:
                winner = game.roundEndCheck("rainbow")
                if winner:
                    print("A player has won by using every possible element this round.")
                    matchEnded = game.roundEndUpdate(winner)
                    if matchEnded:
                        break

            # Ask the player whether they want to activate power up
            activate = input("Do you want to activate power up? Answer with yes or no: ").lower()
            while True:
                if activate == "yes":
                    player.activatePowerUp()
                    break
                elif activate == "no":
                    break
                else:
                    print("You have entered an invalid response. Please try again.")
                    activate = input("Do you want to activate power up? Answer with yes or no: ").lower()

            # Computer randomly decides whether to activate power up or not
            computerActivate = random.choice([True, False])
            if computerActivate:
                computer.activatePowerUp()

            # Check rainbow round end condition
            if game.rainbow:
                winner = game.roundEndCheck("rainbow")
                if winner:
                    print("A player has won by using every possible element this round.")
                    matchEnded = game.roundEndUpdate(winner)
                    if matchEnded:
                        break

            # Winner deals damage to the loser
            game.resolveHPChanges()

            # Check if the round ended after HP changes
            if game.reverse:
                winner = game.roundEndCheck("reverse")
                if winner:
                    print("A player has won by depleting their HP.")
                    matchEnded = game.roundEndUpdate(winner)
            else:
                winner = game.roundEndCheck("normal")
                if winner:
                    print("A player has won by depleting enemy HP.")
                    matchEnded = game.roundEndUpdate(winner)

            # At turn end update stamina progress for each player
            game.updatestaminaProg()

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

def help():
    print("Tactical Arcane Showdown is essentially a rock paper scissors like game played in an elemental setting.")
    print("Matches are played as best of 3.")
    print("On each round each player has 20 HP.")
    print("First player to make their opponent go to 0 HP wins.")
    print("Each element has a different damage value against different elements.")
    print("On each turn, you first propose 3 elements to your opponent.")
    print("Then the damage amounts will be shown in a table.")
    print("After you see that table, all you have to do is choosing your final element.")
    print("Your other two elements don't go to waste though. You can activate power ups.")
    print("Left out proposed elements form up a unique power up that can be activated by consuming stamina.")
    print("Each player starts with 1/5 stamina and gains 1 stamina every other turn.")
    print("There are all sorts of tactics such as armor, dot and healing. Sometimes you can even change the rules.")
    print("Tactical Arcane Showdown tries to offer a deep strategic gameplay over regular rock paper scissors.")
    print("You can check all 36 special power ups from the README file.")
    print("Good luck and have fun player!")

def tas_kagit_makas_Cengizhan_Terzioglu():
    playGame = False
    while True:
        print("Welcome to Tactical Arcane Showdown!")
        print("Select an option from the following:")
        print("1. Play the Game Against a Computer.")
        print("2. Learn the Basics of the Game.")
        print("3. Exit")
        choice = int(input("Enter a number: "))
        if choice == 1:
            playGame = True
            break
        elif choice == 2:
            help()
        elif choice == 3:
            print("Why would you run me if you don't want to play?")
            break
        else:
            print("You entered an invalid option. Please try again.")
        
        if playGame:
            tacticalArcaneShowdown()

tas_kagit_makas_Cengizhan_Terzioglu()