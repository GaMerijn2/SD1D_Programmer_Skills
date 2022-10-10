def your_name_and_age():
    print("Hello you! Whats your name?")
    naam = input("Mijn naam is ")
    print(" ")
    print("-----------------------------------------")
    print("And how old are you?")
    leeftijd = input("Ik ben ")
    print(f"{leeftijd}")

def add(a,b):
    print(a*b)
    print(f"{num1}"*f"{num2}")

print("'A' for yourname")
print("'B' to multiply")
a_or_b = input("")
if a_or_b =="A":
    your_name_and_age()

elif a_or_b =="B":
        num1 = input("Nummer 1: ")
        num2 = input("Nummer 2: ")
        add()
            
