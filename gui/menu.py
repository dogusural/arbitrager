

choice ='0'
while choice =='0':
    print("Please choose currency.")
    print("Choose 1 for TRY")
    print("Choose 2 for EUR")

    choice = input ("Please make a choice: ")

    if choice == "1" or choice == "2":
        print("Please choose arbitrage direction.")
        print("Choose 1 for Turkish -> Europe")
        print("Choose 2 for Europe  -> Turkish")
        choice = input ("Please make a choice: ")
    elif choice == "2":
        print("Do Something 4")
    elif choice == "3":
        print("Do Something 3")
    elif choice == "2":
        print("Do Something 2")
    elif choice == "1":
        print("Do Something 1")
    else:
        print("I don't understand your choice.")

def second_menu():
    print("This is the second menu")