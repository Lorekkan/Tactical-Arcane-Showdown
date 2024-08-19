# Tactical Arcane Showdown
Tactical Arcane Showdown is essentially a rock paper scissors like game played in an elemental setting.
Matches are played as best of 3.
On each round each player has 20 HP.
First player to make their opponent go to 0 HP wins.
Each element has a different damage value against different elements.
On each turn, you first propose 3 elements to your opponent.
Then the damage amounts will be shown in a table.
After you see that table, all you have to do is choosing your final element.
Your other two elements don't go to waste though. You can activate power ups.
Left out proposed elements form up a unique power up that can be activated by consuming stamina.
Each player starts with 1/5 stamina and gains 1 stamina every other turn.
There are all sorts of tactics such as armor, dot and healing. Sometimes you can even change the rules.
Tactical Arcane Showdown tries to offer a deep strategic gameplay over regular rock paper scissors.
You can check all 36 special power ups from the README file.
Good luck and have fun player!

# How To Run
Use an IDE or regular command prompt.
Go to the directory of the source file.
You need to call "pip install tabulate" command in this directory. This will install a necessary library.
On IDE you can simply press Run. If you are using a regular command prompt, use "python tas.py" command.
After following these steps the game should start running. Have fun!

 # All 36 Unique Elemental Power Ups
 Fire-Water: Boiling Point
 Apply Boiling to your enemy. Player with the Boiling chooses their 3 elements before and those elements are shown to their enemy.
 
 Fire-Wind: Drought
 Remove all the buffs from your enemy.
 Fire-Nature: Forest Fire
 Apply Burn to your enemy. Burn can stack infinitely. Burn deals 1 damage for each stack when Nature is actively used and at the start of each turn.
 Fire-Electric: Chip Malfunction
 Values in the point table are reversed.
 Fire-Earth: Meteor Strike
 Add a meteor into the meteor shower this round. Each meteor deals 1 damage to a random player at the start of a turn.
 Fire-Metal: Hephaestus to the Rescue
 Apply Forge to yourself. Forge can stack infinitely. Forge makes you deal 1 additional damage this round. This doesn’t apply to debuffs.
 Fire-Light: Sun Will Shine On Us Again
 Apply Sunshine to yourself. For each stack of Sunshine you deal 2 additional damage this turn. This doesn't apply to debuffs.
 Fire-Dark: Cauldron Upgrade
 Apply Stack+ to yourself. Stack+ makes your debuffs deal 1 additional damage this round.
 Water-Wind: Whirlpool
 Each turn a random element is locked for both players. This effect is dispelled when it's activated again.
 Water-Nature: Rejuvinating Waters
 On win, reduce your damage to half this turn and heal yourself for the original damage amount.
 Water-Electric: Thrown Into an Electric Eel Tank
 Apply Shock to your enemy. Shock can stack infinitely. Shock deals 1 damage for each stack when a powerup is activated and at the start of each turn.
 Water-Earth: Stuck in the Swamp
 On win, rounds needed to recover stamina increases by 1 for your enemy.
 On lose, this debuff is applied to you instead.
 Water-Metal: Shields Are Failing
 On win, remove the enemy armor and deal damage equal to the enemy armor value instead.
 On lose, additionally receive damage equal to the enemy armor value.
 Water-Light: The Dark Side of the Moon
 Add an additional win condition to this round: The player who has actively used (final selection of powerup) each element wins the round.
 Water-Dark: Bermuda Triangle
 Apply Lost to your enemy. Lost locks all the elements selected by the player in the previous turn.
 Wind-Nature: What Goes Around, Comes Around
 This round, when a player goes to 0 health, they win. This effect is dispelled when it’s activated again.
 Wind-Electric: You Are Not Worthy
 When you apply an infinitely stackable buff or debuff this round, apply an additional stack.
 Wind-Earth: Sandstorm
 Apply Dust to your enemy. Dust can stack infinitely. Dust deals 1 damage for each stack when Wind isn't actively used and at the start of each turn.
 Wind-Metal: Industrial Revolution
 On win, rounds needed to recover stamina decreases by 1.
 On lose, it increases by 1 instead.
 Wind-Light: Summer Breeze
 Remove all the debuffs you have.
 Wind-Dark: Zathura
 Summon a black hole. It deals 1 damage to both players at the start of each turn. Black hole's damage is increased after each time this power up is activated.
 Nature-Electric: Spoiled Plants
 Apply 2 stacks of Poisoned to your enemy. Poisoned can stack infinitely. Poisoned deals 2 damage at the start of each turn and loses 1 stack.
 Nature-Earth: Regenerative Tissue
 Apply Herb to yourself. Herb is infinitely stackable. Herb heals you 1 HP for each stack at the start of each turn.
 Nature-Metal: Harvest the Crops
 On win, deal additional damage equal to your armor.
 On lose, lose all your armor before receiving damage.
 Nature-Light: Overgrowing Snapvine
 Apply Trapped to your enemy. Trapped locks the final chosen element of the enemy from previous turn.
 Nature-Dark: Mind Swap
 On win, swap your stats with the opponent, if you have less HP than your enemy.
 On lose, swap your stats with the opponent, if you have more HP than your enemy.
 Stats that change: HP, armor, stamina, brilliance, stamina progress
 Electric-Earth: Hold Any Charges
 If the enemy uses a power up this turn, remove all your debuffs and apply them to your enemy.
 If both players activate this power up, debuff are swapped.
 Electric-Metal: Let Him Cook
 On win, deal double the damage. If the enemy has armor, deal triple the damage instead.
 On lose, receive double the damage. If you have armor, receive triple the damage instead.
 Electric-Light: Daylight Saving Time
 On lose, gain 3 stamina.
 Electric-Dark: Back to the Dark Ages
 On win, disable all future powerups this round.
 On lose, lose all your stamina and stamina earning progress.
 Earth-Metal: Greatest Earth Bender
 On lose, you don’t receive damage this turn.
 On win, you deal half the damage. (rounded down)
 Earth-Light: Come Get Your Armor
 Apply Tough to yourself. Tough can stack infinitely. Tough grants 1 armor to you for each stack at the start of each turn. 
 Earth-Dark: SMASH!
 Apply Quake to your enemy. Quake can stack infinitely. Quake deals 1 damage for each stack when Earth is actively used and at the start of each turn.
 Metal-Light: The Cavalry is Here
 On win, gain armor equal to the damage dealt.
 On lose, gain armor equal to the half of the damage received. (rounded down)
 Metal-Dark: The Dark Knight Rises
 On win, deal half the damage your enemy receives (rounded down) and gain double the amount as armor.
 Light-Dark: Yin and Yang
 Reverse this turn's point.
 
