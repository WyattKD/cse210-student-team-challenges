class Interact:
    """ Handles all interactions with the user and the game, and validates guesses. """
    
    def get_guess():
        """ Gets guess from the user and calls a method to check it's validity. """
        
        validity = False
        while validity == False:
            guess = str(input("Guess a letter [a-z]: "))
            validity = Interact.is_guess_valid(guess.lower())

        if validity == True:
            return guess.lower()

    def is_guess_valid(guess):
        """ Checks if the user's guess is valid. """

        valid_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if guess in valid_list:
            return True
        else:
            print("Invalid response. Please try again.")
            return False

    def add_letter(guess, blank_word, word):
        """ Adds a correctly guessed letter to the blank word. """
        
        for i in word:
            if guess == i:
                blank_word[i] = guess

        return blank_word

    def get_blank_word(word):
        """ Converts the chosen word to blanks to be displayed to the user. """
        
        blank_word = ""

        for i in range(len(word)):
            blank_word += "-"
        
        return blank_word


    def check_win(blank_word):
        """ Checks if every letter in the word has been guessed. """

        win = True
        for i in blank_word:
            if i == "-":
                win = False

        return win

