# flnp
Foreign Language Number Practice

A learning utility that helps you practice translating numbers spoken in a foreign language.

Installation:
Download or clone the repo
cd in and run pip3 install -r requirements.txt

Configure:
Edit config.py to set the language, number range to practice, and delay. Acceptable languages can be found by running the following in an interactive python session:

import gtts

gtts.lang.tts_langs()

Number range to practice is fairly self-explanatory.

Delay refers to a time delay after entering the previous answer before the next number is read. It is in seconds.

Slow controls the speed at which the number is read. Can be set to True or False.

Run:
python3 flnp.py

TODO:
- Installation related stuff (requirements.txt and etc?)
- Use an offline TTS instead of gTTS. Pyttsx3 lets user customize voices and languages, and doesn't require an internet connection. But there are some installation complexities with getting the languages configured. Stick with this unless there is a good Linux-Japanese offline TTS.
- Implement a web or desktop gui. Should be able to edit obvious values like language and number range from gui. More complex stuff can be left in the config.
- Mode where it prints the number written in the language (not numerals) and the user enters the number. But maybe this doesn't make sense for some languages.
- Use lighter audio library. Pygame has a lot of unneeded features. Is there a better choice? Not many libraries can read from a file pointer- it seems most want a real file.
- Decimals and negatives, and config to control them.
- Make the welcome and score messages be read in the language of choice. Should be able to turn off in the config.
