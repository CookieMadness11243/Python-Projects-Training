"""
1- Create a list of words and randomly select one.
2- Initialize variables to store guessed characters and remaining attempts.
3- Display the word using underscores for unguessed characters.
4- Accept a character from the user.
5- Check whether the character exists in the word.
6- Continue until the word is guessed or all attempts are exhausted.
7- Display the result.
"""

word = list("advanced")  # make a list of letters in place

guesses = 0
chances = 7

word2 = ["_" for letter in word]  # used List Comprehension (in case you didn't know that thing existed, there a good documentation here => https://labex.io/pythoncheatsheet/cheatsheet/comprehensions)

print(f"Guess The Word! {" ".join(word2)}") 

while guesses != chances:
    print()  # for better redability
    if word2 == word:
        print(f"you won! the word is {"".join(word)}")
        break
    guess_letter = str(input(f"What's your guess? you have {chances-guesses} chances: "))  # fixed a bug

    if guess_letter in word:
        for CorrectGuess in range(len(word)):
            if guess_letter == word[CorrectGuess]:
                word2[CorrectGuess] = word[CorrectGuess]
        print("Correct!", " ".join(word2))
    elif guesses >= chances:
        print("You Loes :(")  # does'nt show when you lose
        break
    else:
        guesses+=1
        print(f"Wrong, Guesses left {chances - guesses}")  # kinda useless because you already wrote guesses left in line 26
