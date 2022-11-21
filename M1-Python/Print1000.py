while True:
    print("What is 1 + 1?")
    antwoord = int(input("Het antwoord is: ")) 

    if antwoord == "2":
        print(f"{antwoord} is Correct!")
        break
    else:
        print(f"{antwoord} is the Wrong Answer.")
        print(" ")
