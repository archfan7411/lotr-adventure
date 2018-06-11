# LOTR-themed Adventure clone by Joseph Daly, using the MIT license.
#
# Adventure games work by showing text and asking for
# responses. The responses influence the outcome.
#
# To avoid having to write a million possible outcomes,
# our adventure will be randomly generated.

# We begin by importing the random library.

import random

# Then we define our locations.

locations = ["desert","forest","beach","cliff","ancient castle","field","coast","tower","outpost","jungle","crossroads","road","path","grasslands","volcano","cave","cavern","tunnel"]

# Then descriptive adjectives for these locations.

adjectives = ["great","large","small","arid","serene"]

# Then items that we may encounter at these locations.

items = ["axe","sword","dagger","chest","ring","shield","potion","bow","quiver","scroll","scabbard"]

# Prerequisite items (e.g. you need a quiver to use a bow)

bow_pre = "quiver"
sword_pre = "scabbard"
dagger_pre = "scabbard"

prerequisite_items = ["dagger","bow","sword"] # Items that require prerequisites

# Items needed to defeat levels of mob.

unfriendly_items = ["axe","sword","dagger","bow"]
monster_items = ["axe","sword","bow",]

# Items that can be used to gain 5 points (Consumables)

useable_items = ["scroll","potion"]

# Lootbox items that grant a random item

lootbox_items = ["chest"]

# Rewards from opening a lootbox

lootbox_rewards = ["Gandalf's Wooden Staff","The Dagger of Isildur","Thorin's Axe","a Mithril Spear"]

# The player's point total.

points = 0

# Point rewards for killing each type of mob.

reward_unfriendly = 5
reward_monster = 10
reward_boss = 100

# Friendly mobs.

friendly = ["sheep","horse","raven","goat","chicken","eagle","dwarf","hobbit","man","wizard","elf"]

# Unfriendly mobs.

unfriendly = ["cave-claw","orc","goblin","wolf","snake"]

# The REAL deal.

monsters = ["troll","mage","giant tarantula","tyrant"]

# The "boss" mobs - unbeatable except with legendary weapons

bosses = ["Balrog","witch-king","Nazgul","Ringwraith"]

# Mobs that can speak with us

mobs_speak = ["elf","dwarf","hobbit","man","raven","wizard","eagle"]

# Then helpful variables.

mob_types = ["friendly","unfriendly","monsters","bosses"] # Used to tell what we're dealing with.

inventory = ["hand"] # Initializing our weapon inventory with a hand as a weapon.

# Narrator stuff.

narrate_friendly = ["a peaceful","a friendly"]
narrate_unfriendly = ["a mean","an old","a vicious"]
narrate_monsters = ["a terrifying","a terrible","a strong","a warlike"]
narrate_items = ["a old","a rusted","a beautifully carved","a strong"]

# Stuff to handle actions.

action_take = ["TAKE","PICK","GAIN","STEAL","FINGER","SNATCH"]
action_kill = ["KILL","ATTACK","MURDER","AVENGE","STAB","SHOOT","HACK","SLASH","FIGHT","PUNCH","HIT","STRIKE","DEFEAT","SLAY"]
action_converse = ["SPEAK","TALK","CONVERSE"]
action_use = ["READ","USE","DRINK","OPEN"]
action_loot = ["LOOTBOX"]
success = False
action_points = ["POINT"]
action_inv = ["INV"]
moveon = False # Checking if we wish to move on to the next scene.

# Now for the fun stuff.

while(1):

    print("--~~--")
    
    area = random.choice(locations)
    loot = random.choice(items)
    mob_choice = random.choice(mob_types)
    if mob_choice is "friendly":
        mob = random.choice(friendly)
        narrate = narrate_friendly
    if mob_choice is "unfriendly":
        mob = random.choice(unfriendly)
        narrate = narrate_unfriendly
    if mob_choice is "monsters":
        mob = random.choice(monsters)
        narrate = narrate_monsters
    if mob_choice is "bosses":
        mob = random.choice(bosses)
        narrate = narrate_monsters
    # Now we make the text...
    print("You come to a", random.choice(adjectives), area, "where there is", random.choice(narrate), mob, "and", random.choice(narrate_items), loot, "- What do you do?")


    moveon = False

    while(moveon is False):

        response = input(": ")
        response = response.upper()
    
        for item in action_take:
            if item in response:
                if loot in prerequisite_items: # If a prerequisite is needed for this item
                    if loot is "bow":
                        if bow_pre in inventory:
                            inventory.append(loot)
                            print("You pick up the bow since you have a quiver to go with it.")
                        if bow_pre not in inventory:
                            print("You leave the bow there - no use without a quiver.")
                    if loot is "sword":
                        if sword_pre in inventory:
                            inventory.append(loot)
                            print("You pick up the sword. It fits perfectly in the scabbard you found!")
                        if sword_pre not in inventory:
                            print("You look at the sword, but have no way to carry it in the journey ahead.")
                    if loot is "dagger":
                        if dagger_pre in inventory:
                            inventory.append(loot)
                            print("This is a very nice dagger, and it fits quite well in that scabbard.")
                        if dagger_pre not in inventory:
                            print("It's a nice trinket, you have no place to store the dagger.")
                if loot not in prerequisite_items:
                    inventory.append(loot)
                    print("You picked up the", loot)
                moveon = True

        for item in action_kill:
            if item in response:
                if mob_choice is "friendly":
                    points = points - 7
                    print("You can't kill the", mob,"- it's friendly! -7 points.")
                if mob_choice is "unfriendly":
                    # Check if we have the right tools
                    for item in inventory:
                        if item in unfriendly_items:
                            success = True

                    if success is True:
                        points = points + reward_unfriendly # Give more points for the kill.
                        print("With your gear, you killed the", mob, "and gained", reward_unfriendly, "points for a total of", points)

                    if success is False:
                        print("You were outmatched! Quest around to get better gear - no points this time!")

                if mob_choice is "monsters":
                    # One more time we must check the user's tools!
                    for item in inventory:
                        if item in monster_items: #Check if they have good enough gear...
                            success = True
                    if success is True: # If their gear was adequate...
                        points = points + reward_monster
                        print("Your weapons and skills overcame the", mob, "and you gained", reward_monster, "points for a total of", points)

                    if success is False: # If they failed...
                        print("Against this enemy you failed and had to run. Play more to overcome these evils!")

                if mob_choice is "bosses":
                    for item in inventory:
                        if item in lootbox_rewards:
                            chance = [True,False]
                            success = random.choice(chance)

                    if success is True:
                        points = points + reward_boss
                        print("You mightily defeated the", mob, "and gained", reward_boss, "points, for a total so far of", points, "points!")

                    if success is False:
                        points = points - 20
                        print("The power of the", mob, "overcame you, and you were swept aside with severe injury! -20 points.")
                moveon = True

        for item in action_converse:
            if item in response:
                if mob_choice is "friendly":
                    if mob in mobs_speak:
                        points = points + 2
                        print("You had a pleasant conversation with the", mob, "and caught up on the news in Middle-Earth. +2 points.")
                    if mob not in mobs_speak:
                        print("The", mob, "nods in a knowing way but does not utter a word.")
                if mob_choice is not "friendly":
                    points = points - 2
                    print("The", mob, "seems reluctant to engage in conversation. -2 points.")
            moveon = True

        for item in action_use:
            if item in response:
                if loot in useable_items:
                    points = points + 5
                    print("Opening the", loot, "gained you five points!")

                if loot not in useable_items: # If there's nothing to use here
                    print("You couldn't find anything here to use.")
                moveon = True

        for item in action_points:
            if item in response:
                print("Current point total:", points)

        for item in action_inv:
            if item in response:
                print("Your inventory:", inventory)

        for item in action_loot:
            if item in response:
                if loot in lootbox_items:
                    pick = random.choice(lootbox_rewards)
                    inventory.append(pick)
                    print("You open the", loot, "and find", pick)
                moveon = True
                

        if "MOVE ON" in response:
            moveon = True
