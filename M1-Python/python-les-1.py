from datetime import datetime

print("Hello SD1D! Who are you?");
naam=input("Ik ben ")
#print(naam)

print(f"Hallo {naam} In welk jaar ben jij geboren?")
jaar=input("In het jaar ")
#print(jaar)

calc = datetime.now().year - int(jaar)
jaartijd = datetime.now().year 
print(f"het is {jaartijd} dus jij bent {calc} jaar oud." )
