def ask():
        print("Regent het buiten?")
        print(" ")
        antwoord = input()

        if antwoord == "ja":
            print("Bedankt!")

        elif antwoord =="nee":
            print("Bedankt!")

        else:
            print("Dit is geen 'ja' of 'nee'...")
            ask()
ask()