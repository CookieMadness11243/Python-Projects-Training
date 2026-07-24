"""
1- Create a list of words and randomly select one.
2- Initialize variables to store guessed characters and remaining attempts.
3- Display the word using underscores for unguessed characters.
4- Accept a character from the user.
5- Check whether the character exists in the word.
6- Continue until the word is guessed or all attempts are exhausted.
7- Display the result.
"""
# Hello It's me! Abdulmalik.
word = "advanced"
word = list(word)

guesses = 0
chances = 7

# Creating a second list with the name if word2, the array I'll work with to print out the guesses and answers
word2 = word.copy()
for replace in range(len(word)):
    word2[replace] = "_"
print(f"Guess The Word! {" ".join(word2)}")

# Game Loop
while guesses != chances:
    # Win Case:
    if word2 == word:
        print(f"you won! the word is {"".join(word)}")
        break
    guess_letter = str(input(f"What's your guess? you have {chances} chances: "))
    
    # Guessing the right letter
    if guess_letter in word:
        for CorrectGuess in range(len(word)):
            if guess_letter == word[CorrectGuess]:
                word2[CorrectGuess] = word[CorrectGuess]
        print("Correct!", " ".join(word2))
        # Losing all chances
    elif guesses >= chances:
        print("You Loes :(")
        break
        # Guessing wrong
    else:
        guesses+=1
        print(f"Wrong, Guesses left {chances - guesses}")
# import asyncio
