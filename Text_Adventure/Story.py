import time

def lore (save_s,inve,map,stats):
    
    if save_s == 1:
        print(">You have woken up on a splendid day, the sun is shining the flowers are blooming, which makes you wonder, what could go wrong on such a beautiful morning?")
        time.sleep (7)
        print(">You packed your own tent, welcoming your journey ahead.")
        time.sleep (3)
        print(">You scowered your bag for supplies, making a checklist of the items inside:")
        time.sleep (3)
        inve()
        print("[Toggle it anytime with the enter of a lowercase i]")
        time.sleep (2)
        print("This is the world map.")
        time.sleep (1)
        map()
        time.sleep(2)
        print("These are your personal statistics[Toggle it with the enter of a lowercase s]")
        time.sleep(2)
        stats()
        print("Let's Goo!!")
        save_s = 2

    return save_s
