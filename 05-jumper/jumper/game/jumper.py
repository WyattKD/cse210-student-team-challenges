class Jumper:

    def __init__(self):
        self.lives = 4
        self.guesses = []

    def display_jumper(self):
        """
        Displays the jumper on the screen, which acts as the player's lives. Also displays wrong guesses and a 
        game over message.
        """
        four_lives = "\n  ___   "
        three_lives = "\n /___\\"
        two_lives = "\n \\   /"
        one_lives = "\n  \\ /"
        any_lives = "\n   0   \n  /|\\\n  / \\\n\n^^^^^^^"
        no_lives = "\n   x   \n  /|\\\n  / \\\n^^^^^^^"

        guess_line = "\nWrong Guesses: "

        jumper_display = ""
        jumper_lines = [any_lives, one_lives, two_lives, three_lives, four_lives]

        if self.lives <= 0:
            jumper_lines[0] = no_lives
        for line in jumper_lines:
            if jumper_lines.index(line) <= self.lives:
                jumper_display = line + jumper_display
            else:
                jumper_display = "\n" + jumper_display
        if len(self.guesses) > 0:
            for guess in self.guesses:
                guess_line += f"\'{guess}\', "
            guess_line = guess_line[:-2] + "."
        if self.lives == 0:
            guess_line = ""
        jumper_display += guess_line

        return jumper_display

    def correct_guess(self, guess, word):  
        """
        Determines if the player's guess is correct or not, and then appends the guess to the guess list
        """
        if (guess in word) and (guess not in self.guesses):  
            return True
        elif guess not in self.guesses:
            self.guesses.append(guess)
            return False
        else:
            return False

