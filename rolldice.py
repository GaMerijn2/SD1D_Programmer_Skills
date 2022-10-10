import random

def nummer():
    print("Dit is nummer "+ str(random_nummer))

def rollDice():
    return random.randint(0,999)

x = rollDice()
random_nummer = x + 1
nummer()