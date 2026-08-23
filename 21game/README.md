State of project: still isn't complete :(, let's hope that my future self completes it

// __init__.file documentations
  this file contains the functions of both the player and computer and how they'll play with a set of rules
  first the input:
        guess = input("Enter your play(1-3 consecutive nums): ")
  ```then i had an array that turns all the nums in guess to integers:
        guess_list = [int(num) for num in guess]
```
then it checks wether it's a correct play or not where it will loop through all nums
  to check if both are consecutive or not by bringing the second number and applying a minus 1 to it
 ``` and if they are consecutive then it'll just return True, anything else will tell you that it isn't consecutive
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
```
and i still haven't worked on the computer's func:
```
          def computer_function():
              pass
```


// 21game.file documentation

 ```first i grab the libraries:
	from __init__ import player_function, computer_function
	import random
```
 ```then i assigned the values:
	turn = random.randint(1, 2)
	player_turn = False
	computer_turn = False
```
```set the loop:
	game_loop = True
	while game_loop:
```
then the code itself
i first grabbed a random integer to set which should play first
```if it's the computer then it'll be true if player then it'll be true:
    if turn == 1:
        player_turn = True
    else:
        computer_turn = True
```
```then called the function itself which contains the player rules and inputs
    if player_turn == True:
        player_function()
```
