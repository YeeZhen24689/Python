
import time
from random import randint
from random import uniform

if TimesEntered == 1:
    Name = 0
    Age = 0
    Name=input("<SYSTEM> What is your name?")
    if Name == "Skip":
        startingscreen()
    else:
        time.sleep (2)
        print("<SYSTEM> '",Name,"'", "what a nice name.")
        time.sleep (2)
        Age=input("<SYSTEM> What is your current age?")
        print("<SYSTEM> DATA SUCESSFULLY LOGGED")
        TimesEntered = 0
        print("--------------------------------")
        time.sleep (2)
        print("<???> Welcome",Name)
        time.sleep (2)
        print("<???> This will be the first time I meet you in person.(Well I technically can't because I am a coded entity.)")
        time.sleep (4)
        print("<???> Call me Bob.")
        time.sleep (2)
        print("<Bob> It's time to play the game, shall we?")
        time.sleep (2)
        startingscreen()
else:
    print(NameSave)
    print("Welcome Back",Name,"!")
    time.sleep(1)
    startingscreen()