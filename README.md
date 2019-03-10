# flnp
Foreign Language Number Practice

A learning utility that helps you practice your numbers in foreign languages.

TODO:
- Installation related stuff (requirements.txt and etc?)
- Config file
- Use pyttsx3 instead of gTTS 
    pyttsx3 lets user customize voices and languages, and doesn't require an internet connection. But there are some installation complexities with getting the languages configured.
- Web or desktop gui
    Should be able to edit obvious values like language and number range from gui. More complex stuff can be left in the config.
- Mode where it prints the number written in the language (not numerals) and the user enters the number.
    But maybe this doesn't make sense for some languages? Not sure
- Use lighter audio library
    Pygame has a lot of unneeded features. Is there a better choice? Not many libraries can read from a file pointer- it seems most want a real file.
