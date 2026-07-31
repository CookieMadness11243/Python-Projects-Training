game_arr = []

def player_function():
    guess = str(input("Enter your play(1-3 consecutive nums): "))
# are nums consecutive and from 1 to 3
    guess_list = [int(num) for num in guess]
    if len(guess) <= 3:
        for i in range(len(guess) - 1):
            if guess_list[i] == guess_list[i + 1] - 1:
                print(guess_list[i], guess_list[i + 1] - 1)
                print(True)
            else:
                print(guess_list[i], guess_list[i + 1] - 1)
                print(False)
    else:
        print("Try Again")
        player_function() 

def house(name):
    print(f"Hello {name}")