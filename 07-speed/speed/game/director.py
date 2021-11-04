from time import sleep
import random
import raylibpy
from game.word import Word
from game import constants
from game.word import Word
from game.score_board import ScoreBoard
from game.buffer import Buffer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        food (Food): The snake's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        snake (Snake): The player or snake.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score_board = ScoreBoard()
        self._buffer = Buffer()
        self._word = Word()
        self._words = []

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        print("Starting game...")
        self._output_service.open_window("Speed")

        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

            if self._input_service.window_should_close():
                self._keep_playing = False

        print("Game over!")

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        letter = self._input_service.get_letter()
        self._buffer.update_buffer(letter)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """

        self.generate_new_word()
        self.remove_matches()
        self.remove_lost_words()

        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._buffer)

        self._output_service.flush_buffer()
        self._output_service.draw_actor(self._word)
        self._output_service.draw_actor(self._score_board)
        self._output_service.draw_actors(self._words)
        self._output_service.flush_buffer()

    def remove_matches(self):
        words_to_remove = []
        for word in self._words:
            if self._buffer.check_for_match(word):
                words_to_remove.append(word)
                # add points to score
        for word in words_to_remove:
            self._words.remove(word)

    def remove_lost_words(self):
        words_to_remove = []
        for word in self._words:
            if word.is_off_screen():
                words_to_remove.append(word)
                # subtract points from score
        for word in words_to_remove:
            self._words.remove(word)

    def generate_new_word(self):
        pass

