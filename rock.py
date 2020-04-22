import random
while True:
    choice = input("Hey what is yor choice ")
    # print(choice)
    choice = choice.lower()
    choices = ['rock','paper','scissors']
    # computer_choice = choices[random.randint(0,len(choices)-1)]
    computer_choice = random.choice(choices)
    print(computer_choice)
    if choice in choices:
        if computer_choice == choice:
                print("its a tie")
        if choice == "rock":
            if computer_choice == "scissors":
                print("You win")
            elif computer_choice == "paper":
                print("You lose, sorry")
        elif choice == "paper":
            if computer_choice == "scissors":
                print("You lose sorry")
            elif computer_choice == "paper":
                print("You win")
        elif choice == "scissors":    
            if computer_choice == "paper":
                print("You win")
            elif computer_choice == "rock":
                print("You lose, sorry")
    else:
        print("Sorry but you have to quit")
    print()