
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
