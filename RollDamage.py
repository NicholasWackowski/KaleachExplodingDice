# Nicholas Wackowski, 8/9/2020
# Using a combination of the Great Weapon Master and Exploding Dice mechanics,
# this code simulates rolling damage rolls for the BBEG of my campaign so that
# it is automated and much quicker.

# First 3d4 are rolled, then they are linearly evaluated. First check if the 
# die is a 1 or 2, replace that entry with a new d4 result. Then, if the
# result was a '4', push another d4 onto the stack.
# Once the whole stack is verified, return the sum.

import random
from datetime import datetime
random.seed(datetime.now())

# Return a random number from [1-4]
def rolld4():
    return random.randrange(4)+1

# Return a random number from [1-6]
def rolld6():
    return random.randrange(6)+1

def rollDamage(isCrit, slashingMod, psychicMod):
    damageRolls = []
    
    # The default number of dice rolled
    numd4 = 3
    numd6 = 2
    
    # If the attack is a critical, change num dice rolled
    if(isCrit):
        numd4 = 6
        numd6 = 4
        
    # Roll the initial d4's
    for x in range(0, numd4):
        damageRolls.append(rolld4())
        
    # Linearly evaluate each die.
    for index, die in enumerate(damageRolls):
        # If 1 or 2, reroll and replace
        if(die == 1 or die == 2):
            damageRolls[index] = rolld4()
        # If 4, append a new roll to the list
        if(damageRolls[index] == 4):
            damageRolls.append(rolld4())
    slashingDamage = sum(damageRolls)+slashingMod
    
    # Add the psychic damage (2d6 by default)
    # (not affected by exploding dice or HWM)
    psychicDamageRolls = []
    for x in range(0, numd6):
        psychicDamageRolls.append(rolld6())
    psychicDamage = sum(psychicDamageRolls)+psychicMod
    totalDamage = slashingDamage+psychicDamage
    print(damageRolls, psychicDamageRolls)
    print("Total damage:", totalDamage)
    print("Slashing:", slashingDamage)
    print("Psychic:", psychicDamage)
    return sum(damageRolls)+sum(psychicDamageRolls)+slashingDamage+psychicDamage

def main():
    STR = 4 # Strength modifier
    ENH = 3 # Enchancement bonus to damage
    CHA = 5 # CHA bonus to damage
    rollDamage(isCrit=False, slashingMod=STR+ENH, psychicMod=CHA)
    
main()