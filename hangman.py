#Hangman

#A variable to store the word, the player is going to guess.
wordToGuess = "hello"

#A function to initialize the variables.
def InitializeVariables():
    wordToGuess.upper()
    global lengthOfWord
    lengthOfWord = len(wordToGuess)
    global numberOfGuessesLeft
    numberOfGuessesLeft = 9
    global correctLettersGuessed
    correctLettersGuessed = []
    global incorrectLettersGuessed
    incorrectLettersGuessed = []
    global guessedWords
    guessedWords = []
    global showCorrectLettersGuessedInWord
    showCorrectLettersGuessedInWord = []

#A function to ask the player to guess a letter.
def GuessLetter():
    while True:
        try:
            letterGuessed = str(input("Please enter a letter to guess? "))
        except ValueError:
            print("You have not entered a letter.")
            continue
        else:
            if len(letterGuessed) != 1:
                print(letterGuessed)
                print("You have entered " + str(letterGuessed) + " which is more than one letter.")
                continue
            elif not letterGuessed.isalpha():
                print("You have entered " + str(letterGuessed) + " which is not a letter")
                continue
            elif letterGuessed in correctLettersGuessed or letterGuessed in incorrectLettersGuessed:
                print("You have already guessed the letter " + letterGuessed + ".")
                continue
            else:
                if letterGuessed in wordToGuess:
                    showCorrectLettersGuessedInWord.clear()
                    print("The letter " + letterGuessed + " you have guessed is correct.")
                    correctLettersGuessed.append(letterGuessed)
                    howManyCorrectLettersGuessed = len(correctLettersGuessed)
                    for letter in wordToGuess:
                        countIterations = 1
                        for correctLetter in correctLettersGuessed:
                            if letter == correctLetter:
                                showCorrectLettersGuessedInWord.append(letter + " ")
                            else:
                                if howManyCorrectLettersGuessed == countIterations:
                                    howManyCorrectLettersGuessed  
                                    showCorrectLettersGuessedInWord.append("_ ")
                                countIterations += 1
                    outputCorrectLettersGuessedInWord = "".join(showCorrectLettersGuessedInWord)
                    outputCorrectLettersGuessedInWord.upper()
                    print(outputCorrectLettersGuessedInWord)
                    if "_" not in outputCorrectLettersGuessedInWord:
                        print("You have guessed all of the letters, and the word to guess was " + wordToGuess + ", you have won.")
                        PlayAgainQuestion()
                    else:
                        GuessLetterOrWordQuestion()
                else:
                    print("The letter " + letterGuessed + " you have guessed is incorrect.")
                    global numberOfGuessesLeft
                    numberOfGuessesLeft -= 1
                    incorrectLettersGuessed.append(letterGuessed)
                    if numberOfGuessesLeft == 0:
                        print("You have " + str(numberOfGuessesLeft) + " guesses left, you have lost. The word was " + wordToGuess + ".")
                        PlayAgainQuestion()
                    else:
                        print("You have " + str(numberOfGuessesLeft) + " guesse(s) left")
                        GuessLetterOrWordQuestion()
                       
#A function to ask the player to guess a word.                    
def GuessWord():
    while True:
        try:
            wordGuessed = str(input("Please enter the word to guess? "))
        except ValueError:
            print("You have not entered a letter.")
            continue
        else:
            if not wordGuessed.isalpha():
                print("You have entered " + str(wordGuessed) + ", which contains a non alpha character.")
                continue
            elif wordGuessed in guessedWords:
                    print("You have already guessed the word " + wordGuessed + ".")
                    continue
            elif wordGuessed in correctLettersGuessed or wordGuessed in incorrectLettersGuessed :
                    print("You have already guessed the letter " + wordGuessed + ", when you guessed a letter in a previous guess.")
                    continue
            elif wordGuessed == wordToGuess:
                    print("The word " + wordGuessed + " you have guessed is correct, you have won.")
                    PlayAgainQuestion()
            else:
                print("The word " + wordGuessed + " you have guessed, is incorrect.")
                global numberOfGuessesLeft
                numberOfGuessesLeft -= 1
                guessedWords.append(wordGuessed)
                if numberOfGuessesLeft == 0:
                    print("You have " + str(numberOfGuessesLeft) + " guesses left, you have lost. The word was " + wordToGuess + ".")
                    PlayAgainQuestion()
                else:
                    print("You have " + str(numberOfGuessesLeft) + " guesse(s) left.")
                    GuessLetterOrWordQuestion()
                   
#A function to ask the player to guess a letter, or a word.
def GuessLetterOrWordQuestion():
    print("\n")
    guessLetterOrWord = str(input("Would you like to guess a letter or the word? please press L for letter, or W for word and then press enter. "))
    if guessLetterOrWord in ('L','l'):
        GuessLetter()
    elif guessLetterOrWord in ('W','w'):
        GuessWord()
    else:
        print("You have entered " + str(guessLetterOrWord) + ".")
        GuessLetterOrWordQuestion()

#A function to ask the player to play again.
def PlayAgainQuestion():
    print("\n")
    playAgain = str(input("Would you like to play again? please press Y for Yes, or N for No and then press enter. "))
    if playAgain in ('Y','y'):
        InitializeVariables()
        GuessLetterOrWordQuestion()
    elif playAgain in ('N','n'):
        input("Press any key and then press enter to exit.")
        sys.exit()
    else:
        print("You have entered " + playAgain + ".")
        PlayAgainQuestion()

#Starts the Hangman game.
InitializeVariables()
print("Hangman")
print("\n")
print("You have " + str(numberOfGuessesLeft) + " guesses")
print("\n")
print(lengthOfWord * "_ ")
print("Guess the " + (str(lengthOfWord) + " letter word"))
GuessLetterOrWordQuestion()
