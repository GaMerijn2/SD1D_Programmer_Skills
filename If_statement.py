nummer_a=input("Vul nummer A in: ")
print(f"Dit is nummer A: {nummer_a}")

print(" ")

nummer_b=input("Vul nummer B in: ")
print(f"dit is nummer B: {nummer_b}")

print(" ")

if nummer_a > nummer_b:
     print(f"Nummer {nummer_a} is groter dan {nummer_b}.")
elif nummer_a < nummer_b:
    print(f"Nummer {nummer_a} is kleiner dan {nummer_b}.")
elif nummer_a == nummer_b:
    print(f"{nummer_a} en {nummer_b} zijn gelijk.")
else:
    print("Dit is geen nummer...")