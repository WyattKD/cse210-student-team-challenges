from time import time
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
        self._start_time = round(time())
        self._time_to_wait = 10

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        print("Starting game...")
        self._output_service.open_window("Speed")
        for i in range(5):
            self._generate_new_word(True)
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

        self._generate_new_word(False)
        self._remove_matches()
        self._remove_lost_words()
        self._move_words()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._buffer)
        self._output_service.draw_actor(self._score_board)
        self._output_service.draw_actors(self._words)
        self._output_service.flush_buffer()

    def _remove_matches(self):
        words_to_remove = []
        for word in self._words:
            if self._buffer.check_for_match(word):
                self._score_board.add_points(word.get_points())
                words_to_remove.append(word)
        for word in words_to_remove:
            self._words.remove(word)

    def _remove_lost_words(self):
        words_to_remove = []
        for word in self._words:
            if word.is_off_screen():
                self._score_board.add_points(-5)
                words_to_remove.append(word)
        for word in words_to_remove:
            self._words.remove(word)

    def _generate_new_word(self, override):
        if round(time()) - self._start_time  >= self._time_to_wait or override:
            word = Word()
            if override:
                word.starting_five()
            self._words.append(word)
            self._start_time = round(time())
            self._time_to_wait = random.random() + random.randint(0,1)


    def _move_words(self):
        for word in self._words:
            word.move_next()
            word.screen_bounce()


