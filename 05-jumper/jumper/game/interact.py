class Interact:
    
    def get_guess():
        validity = False
        while validity == False:
            guess = str(input("Guess a letter [a-z]: "))
            validity = is_guess_valid(guess)

        if validity == True:
            return guess

    def is_guess_valid(guess):
        valid_list = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        if guess.lower in valid_list:
            return True
        else:
            print("Invalid response. Please try again.")
            return False

    def convert_to_blanks(word):
        blank_word = ""

        for i in range(len(word)):
            blank_word += "_ "
        # print(f"{blank_word}")
        
        return blank_word

    def check_win():
        pass

