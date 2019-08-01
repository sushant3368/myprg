import random
print("\tWelcome to End Game")
print("\tYou are Trapped!!!!! \n \tYou have 3 choices!!!!!")
print('| A Dragon Room(Type dr) | A Bear Room(Type br) | Exit(Type e) |')
while True:
    choice = input("Your Choice Here: ")
    if choice == "dr":
        while True:
            print("Do you want to fight a)Fire Dragon or b)Ice Dragon?")
            dragon = input("Which Dragon?: ")
            if dragon == "a":
                l = ["You Win","You Die"]
                print(random.choice(l))
                break
            elif dragon == "b":
                print("You Win")
                break
            else:
                print("Please Select a Dragon")
        break
    elif choice == " br":
        while True:
            print("Do you want to fight a)Brown Bear or b)White Bear?")
            bear = input("Which Bear?: ")
            if bear == "a":
                while True:
                    print("Do you want to fight or not fight?")
                    yn = input("yes/no: ")
                    if yn == "yes":
                        print("You Win")
                        break
                    elif yn == "no":
                        print("You Loose")
                        break
                    else:
                        print("Please Select yes/no")
                break
            elif bear == "b":
                print("You Win")
                break
            else:
                print("Please Select a Bear")
        break
    elif choice == "e":
        print("You Die")
        break
    else:
        print("Please give your Choice")