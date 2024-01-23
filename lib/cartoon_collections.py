dwarves = ["Doc", "Dopey", "Bashful", "Grumpy"]

def roll_call_dwarves(dwarves):
    for dwarf in dwarves:
        print(f"{dwarves.index(dwarf) + 1}. {dwarf}")

roll_call_dwarves(dwarves)

def summon_captain_planet(planeteer_calls):
    edited = [item.capitalize() + "!" for item in planeteer_calls]
    print(edited)

summon_captain_planet(planeteer_calls = ["earth", "wind", "fire", "water", "heart"])

def long_planeteer_calls(calls):
    for item in calls:
        if len(item) > 4:
            return True
    return False

short_words = ["puff", "go", "two"]
assorted_words = ["two", "go", "industrious", "bop"]

print(long_planeteer_calls(short_words))

def find_the_cheese(snacks):
    cheese = ["cheddar","gouda","camebert"]
    for item in snacks:
        if item in cheese:
            return item

snacks = ["crackers", "gouda", "thyme"]
soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]

print(find_the_cheese(soup))
