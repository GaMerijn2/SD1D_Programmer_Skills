import os

lijstje = []

def add():
    toevoegen = input("Dit voeg ik toe: ")
    lijstje.append(toevoegen)
    vragen()

def verw():
    print("het eerste product uit het lijstje is 0, de tweede is 1, de derde is 2. etc.")
    verwijderen = input("Dit haal ik weg: ")
    lijstje.pop(int(verwijderen))
    vragen()

def lijst_verw():
    lijstje.clear()
    vragen()

def opnieuw():
    print("Sorry, dit begrijp ik niet. Probeer het nog een keer.")
    print(" ")
    vragen()


def vragen():
    os.system('cls')
    print(f"Dit is je lijstje nu: {lijstje}.")
    print(" ")
    print("Wil je iets toevoegen aan je lijstje? ")

    nieuw_item = input()
    if nieuw_item == "ja":
        add()
        print(" ")
    elif nieuw_item =="nee":
        print(f"Dit is je lijstje nu: {lijstje}.")
        print(" ")
        print("Wil je iets verwijderen uit je lijst? ")
        item_verwijderen = input()
        if item_verwijderen == "ja":
            verw()
        elif item_verwijderen == "nee":
            print(f"Dit is je lijstje nu: {lijstje}.")
            print(" ")
            print("Wil je je lijst helemaal verwijderen?")
            lijst_verwijderen = input()
            if lijst_verwijderen == "ja":
                lijst_verw()
            elif lijst_verwijderen == "nee":
                print("Wil je je lijstje zien? ")
                lijstje_zien = input()
                if lijstje_zien == "ja":
                    print(f"Dit is je lijstje: {lijstje}.")
    else:
        opnieuw()
vragen()