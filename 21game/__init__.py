def player_function():
    guess = input("Enter your play(1-3 consecutive nums): ")  # are nums consecutive and from 1 to 3
    
    if guess.isalnum():  # checks if guess have only numbers
        if len(guess) > 3:
            print("Try Again")
            player_function()  # better readability
            return  # for short circuit

        guess_list = [int(num) for num in guess]
        for i in range(len(guess) - 1):
            if guess_list[i] == guess_list[i + 1] - 1:
                print(guess_list[i], guess_list[i + 1])
                print(True)
            else:
                print(guess_list[i], guess_list[i + 1])
                print(False)
                    

def computer_function():
    pass

player_function()
