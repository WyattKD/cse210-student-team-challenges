class Interact:
    """ Handles all interactions with the user and the game, and validates guesses. """
    
    def get_guess(self):
        """
        Gets the user's guess as a single letter string
        """
        validity = False
        while validity == False:
            guess = str(input("Guess a letter [a-z]: "))
            validity = self.is_guess_valid(guess.lower())

        if validity == True:
            return guess.lower()

    def is_guess_valid(self, guess):
        """
        Determines if the guess is valid
        """
        valid_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if guess in valid_list:
            return True
        else:
            print("Invalid response. Please try again.")
            return False

    def add_letter(self, guess, blank_word, word):
        """
        Adds a correctly guessed letter to the blank word
        """
        for index, letter  in enumerate(word):
            if guess == letter:
                blank_word = blank_word[:index] + guess + blank_word[index + 1:]

        return blank_word

    def get_blank_word(self, word):
        """
        Creates a blank word based on the actual word
        """
        blank_word = ""

        for i in range(len(word)):
            blank_word += "-"
        
        return blank_word

    def check_win(self, blank_word):
        """
        Checks if the player has guessed all the letters or not
        """
        win = False
        for i in blank_word:
            if i == "-":
                win = True

        return win

