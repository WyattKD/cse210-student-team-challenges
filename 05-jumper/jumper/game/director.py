# from game. import

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        seeker (Seeker): An instance of the class of objects known as Seeker.
        hider (Hider): An instance of the class of objects known as Hider.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.jumper = Jumper()
        self.interact = Interact()
        self.word_bank = WordBank()
        self.keep_playing = True
        self.user_guess = ""
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means moving the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        word = self.word_bank.get_word()
        blank_word = self.interact.convert_to_blanks(word)
        self.console.write(blank_word)
        jumper_display = self.jumper.display_jumper()
        self.console.write(jumper_display)
        self.user_guess = self.interact.get_guess()
        

    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the hider watches the seeker.

        Args:
            self (Director): An instance of Director.
        """
        if self.jumper.correct_guess(self.user_guess):
            blank_word = self.interact.add_letter(self.user_guess)
        else:
            self.jumper.lose_life()

        
        

    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the hider provides a hint.

        Args:
            self (Director): An instance of Director.
        """

        self.keep_playing = self.interact.is_word_guessed()
        self.keep_playing = self.jumper.is_game_over()

