class Board:

    def __init__(self):
        self.turn = 2
        self.player_1 = ""
        self.player_2 = ""
        self.guess_1 = ""
        self.guess_2 = ""
        self.hint_1 = ""
        self.hint_2 = ""

    def to_string(self):
        # Returns a large string containing {player_1}: {guess}, {hint} that will be printed by the console
        return f"--------------------\nPlayer {self.player_1}: {self.guess_1}, {self.hint_1}\nPlayer {self.player_2}: {self.guess_2}, {self.hint_2}\n--------------------"

    def apply(self, guess, hint):
        # changes the guess and hint for the current player and then switches the current player
        # so that next time this function is called the other player's guess and hint is changed
        if self.turn == 1:
            self.guess_1 = guess
            self.hint_1 = hint
            self.turn = 2
        else:
            self.guess_2 = guess
            self.hint_2 = hint
            self.turn = 1


    def add_name(self, name, player_number):
        # Sets the names of player 1 and player 2, player_number will either be 1 or 2
        if player_number == 1:
            self.player_1 = name
        else:
            self.player_2 = name
