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

#TODO: read from config
lang = 'ja' 
min_num = 0
max_num = 9999
delay = 2

print("Ctrl+C to quit.")

pygame.mixer.init()

try:
        while True:
                num = random.randint(min_num, max_num)
                mp3_fp = io.BytesIO()
                tts = gtts.gTTS(str(num), lang)
                tts.write_to_fp(mp3_fp)
                mp3_fp.seek(0)
                pygame.mixer.music.load(mp3_fp)
                pygame.mixer.music.play()
                while pygame.mixer.get_busy():
                    time.sleep(1)
                ans = input("Please enter your answer: ")
                if ans != num:
                        print("Sorry, the correct answer was " + str(num))
                else:
                        print("Correct!")
                time.sleep(2)
except KeyboardInterrupt as e:
        print("Thanks for learning!")
