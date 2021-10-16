class Jumper:
    """ Handles the jumper display, keeps track of lives, and stores correct guesses. """

    def __init__(self):
        """ Initialization method. """

        self.lives = 4
        self.guesses = []
    
    def display_jumper(self):
        """ Displays jumper graphics to the screen depending on the amount of lives left. """

        four_lives = "\n  ___   "
        three_lives = "\n /___\\"
        two_lives = "\n \\   /"
        one_lives = "\n  \\ /"
        any_lives = "\n   0   \n  /|\\\n  / \\\n\n^^^^^^^"
        no_lives = "\n   x   \n  /|\\\n  / \\\n^^^^^^^"

        guess_line = "\nGuessed Letters: "

        jumper_display = ""
        jumper_lines = [any_lives, one_lives, two_lives, three_lives, four_lives]

        if self.lives <= 0:
            jumper_lines[0] = no_lives
        for line in jumper_lines:
            if jumper_lines.index(line) <= self.lives:
                jumper_display = line + jumper_display
            else:
                jumper_display = "\n" + jumper_display

        for guess in self.guesses:
            guess_line += f"\'{guess}\', "
        guess_line = guess_line[:-2] + "."
        jumper_display += guess_line

        return jumper_display
    
    def correct_guess(self, guess, word):
        """ Checks for correct guesses and stores for later use. """

        if (guess in word) and (guess not in self.guesses):  
            self.guesses.append(guess)
            return True
        else:
            self.guesses.append(guess)
            return False