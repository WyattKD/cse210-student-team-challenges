import os
os.environ['RAYLIB_BIN_PATH'] = r'C:\Users\ethan\OneDrive\Desktop\cse210-student-solo-checkpoints\07-snake\raylib-2.0.0-Win64-mingw\lib'
from game.director import Director
from game.input_service import InputService
from game.output_service import OutputService

def main(screen):
    input_service = InputService(screen)
    output_service = OutputService(screen)
    director = Director(input_service, output_service)
    director.start_game()

Screen.wrapper(main)