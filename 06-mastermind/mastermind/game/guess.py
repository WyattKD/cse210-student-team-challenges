import random

class Guess:

    def __init__(self, digits):
        self._guess = []
        self._hint = []
        self.digits = digits
        self._code = self._prepare()

    def _prepare(self):
        # creates the random 4 digit code between 1000 and 9999
        code = []
        for i in range(1, self.digits + 1):
            if i == 1:
                code.append(str(random.randint(1,9)))
            else:
                code.append(str(random.randint(0,9)))
        return code

    def set_guess(self, guess):
        # splits up the guess and sets the _guess variable
        self._guess.clear()
        for digit in guess:
           self._guess.append(digit) 

    def set_hint(self):
        # sets the _hint variable to a hint based on the _guess
        self._hint.clear()
        for index, digit in enumerate(self._guess):
            if digit == self._code[index]:
                self._hint.append("x")
            elif digit in self._code:
                self._hint.append("o")
            else:
                self._hint.append("*")

    def check_win(self):
        # returns true if _guess matches _code
        guess = "".join(self._guess)
        code = "".join(self._code)
        if guess == code:
            return True
        else:
            return False

    def is_invalid(self, guess):
        # checks if the player's guess is a 4 digit number
        if len(guess) != self.digits:
            return True
        elif not guess.isdecimal():
            return True
        else:
            return False
        


    def get_guess(self):
        # converts the _guess list into a single string and returns it
        return "".join(self._guess)

    def get_hint(self):
        # converts the _hint list into a single string and returns it
        return "".join(self._hint)