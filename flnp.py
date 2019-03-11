import gtts
import io
import random
import sys
import time

#this line prints a message we don't want
old_stdout = sys.stdout
sys.stdout = None
import pygame
sys.stdout = old_stdout

import config as cfg

if __name__ == "__main__":
        print("Ctrl+C to quit.")

        pygame.mixer.init()

        correct = 0
        incorrect = 0

        try:
                while True:
                        num = random.randint(cfg.min_num, cfg.max_num)
                        mp3_fp = io.BytesIO()
                        try:
                                tts = gtts.gTTS(str(num), cfg.lang, cfg.slow)
                        except Exception as e:
                                print("Connection error. Please check internet connection and try again later.")
                                sys.exit(1)

                        tts.write_to_fp(mp3_fp)
                        mp3_fp.seek(0)
                        pygame.mixer.music.load(mp3_fp)
                        pygame.mixer.music.play()
                        while pygame.mixer.get_busy():
                            time.sleep(1)
                        ans = input("Please enter your answer: ")
                        try:
                                if int(ans) != num:
                                        print("Sorry, the correct answer was " + str(num))
                                        incorrect += 1
                                else:
                                        print("Correct!")
                                        correct += 1
                        except ValueError as e:
                                print("Sorry, the correct answer was " + str(num))
                                incorrect += 1

                        time.sleep(cfg.delay)
        except KeyboardInterrupt as e2:
                print("Thanks for learning!\nCorrect: " + str(correct) + "\nIncorrect: " + str(incorrect))
