import random
words =['watermelon','sugarApple','strawberries','pomegranate','pineapple','pear','orange','papaya','lychee','mango','grapes','guava','banana','apple']
guess_word = []
secretWord = random.choice(words) # randomize single word from the list
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []
def change():
    for character in secretWord: # printing blanks for each letter in secret word
        guess_word.append("-")
    print("Ok, so the word You need to guess has", length_word, "characters")
    print("Be aware that You can enter only 1 letter from a-z\n")
    print(guess_word)
def guessing():
    guess_taken = 1
    while guess_taken < 10:
        guess = input("Pick a letter>").lower()
        if guess not in alphabet: #checking input
            print("Enter a letter from a-z alphabet")
        else: 
            letter_storage.append(guess)
            if guess in secretWord:
                print("You guessed correctly!")
                for x in range(0, length_word): 
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)
                if '-'not in guess_word:
                    print("You won!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                if guess_taken == 10:
                    print(" Sorry Mate, You lost :<! The secret word was",secretWord)
change()
guessing()
print("Game Over!")
