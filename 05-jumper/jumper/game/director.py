from game.console import Console
from game.interact import Interact
from game.jumper import Jumper
from game.word_bank import WordBank

class Director:
    """
    Stereotype:
        Controller
    """
    def __init__(self):
        """
        The class constructor.
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.jumper = Jumper()
        self.interact = Interact()
        self.word_bank = WordBank()
        self.keep_playing = True
        self.user_guess = ""
        self.word = self.word_bank.words
        self.blank_word = self.interact.get_blank_word(self.word)
        
    def start_game(self):
        """
        Starts the game loop to control the sequence of play.
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        

    def get_inputs(self):
        """
        Gets the inputs at the beginning of each round of play.
        Args:
            self (Director): An instance of Director.
        """
        self.console.write(self.blank_word)
        jumper_display = self.jumper.display_jumper()
        self.console.write(jumper_display)
        self.user_guess = self.interact.get_guess()
        

    def do_updates(self):
        """
        Updates the important game information for each round of play.
        Args:
            self (Director): An instance of Director.
        """
        if self.jumper.correct_guess(self.user_guess, self.word):
            self.blank_word = self.interact.add_letter(self.user_guess, self.blank_word, self.word)
        else:
            self.jumper.lives -= 1

        
        

    def do_outputs(self):
        """
        Outputs the important game information for each round of play.
        Args:
            self (Director): An instance of Director.
        """
        if self.jumper.lives == 0:
            jumper_display = self.jumper.display_jumper()
            self.console.write(jumper_display)
            self.console.write(f"The word was \'{self.word}\' You Lose!")
            self.keep_playing = False
        else:
            jumper_display = self.jumper.display_jumper()
            self.console.write(jumper_display)
            if not self.interact.check_win(self.blank_word):
                self.keep_playing = False
                self.console.write(f"The word was \'{self.word}\' You Win!")
        