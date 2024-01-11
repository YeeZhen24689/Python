def randomeny():
    global EnHP
    global ShldBlokEn
    global Enem
    global enemyheal
    global healcounten
    global OriEnWea
    global UnivEnWea
    enemy=randint(1,3)
    if enemy == 1:
        print("----------------------")
        time.sleep(1)
        print("A Wombie has appeared!")
        time.sleep(1)
        ShldBlokEn = 2
        Enem = "Wombie"
        EnHP = 25
        enemyheal = 2
        healcounten = 10
        OriEnWea = 10*UnivEnWea
        fight()
    elif enemy == 2:
        print("------------------------")
        time.sleep(1)
        print("A Beegrock has appeared!")
        time.sleep(1)
        ShldBlokEn = 2
        Enem = "Beegrock"
        EnHP = 100
        enemyheal = 2
        healcounten = 15
        OriEnWea = 3*UnivEnWea
        fight()
    elif enemy == 3:
        print("------------------")
        time.sleep(1)
        print("An A has appeared!")
        time.sleep(1)
        ShldBlokEn = 5
        Enem = "A"
        EnHP = 1
        enemyheal = 10
        healcounten = 70
        OriEnWea = 2*UnivEnWea
        fight()
    else:
        print("This message should not appear.")
        
        
def randomloot():
    global basicweapon
    global ultimateweapon
    global equip
    global loot
    global OriP1Wea
    global OriEnWea
    global UnivEnWea
    global ShldBlok
    loot=randint(1,100)
    if loot >= 98:
        ultimateweapon=randint(1,3)
        if ultimateweapon==1:
            print("You have found the Ultra Sword!!")
            time.sleep(2)
            print("[ULTRA SWORD]")
            print("Base Damage Change: 500HP/hit")
            print("A legendary sword meticulously forged by a fallen society that")
            print("once took over the woodlands, it seems really well maintained ")
            print(", most likely got stolen from its former owners.")
            while equip == "NAN":
                equip=input("Equip it? [X] No thank you [Y]")
                if equip == "X":
                    OriP1Wea=500
                    ShldBlok = 2
                    UnivEnWea = 1
                    equip = "NAN"
                    basicweapon = "Ultra Sword"
                    game()
                elif equip == "Y":
                    print("You discarded the weapon reluctantly onto the mold infested ground.")
                    equip = "NAN"
                    game()
                else:
                    print("Invalid Response")
                    equip = "NAN"
        elif ultimateweapon==2:
            print("You have found the Rain-Bow!!")
            time.sleep(2)
            print("[RAIN-BOW]")
            print("Base Damage Change: 60 dmg/hit")
            print("Perks : You gain invulnerability to enemy damage")
            print("A mystical bow that just randomly fell down on your head for ")
            print("some odd reason. Summons an invulnerability sheild around the player.")
            while equip == "NAN":
                equip=input("Equip it? [X] No thank you [Y]")
                if equip == "X":
                    OriP1Wea = 60
                    ShldBlok = 2
                    UnivEnWea = 0
                    equip = "NAN"
                    basicweapon = "Rain-Bow"
                    game()
                elif equip == "Y":
                    print("You discarded the weapon reluctantly onto the mold infested ground.")
                    equip = "NAN"
                    game()
                else:
                    print("Invalid Response")
                    equip = "NAN"
        elif ultimateweapon == 3:
            print("You have found the Uno Reverse Card!!")
            time.sleep(2)
            print("[UNO-REVERSE CARD]")
            print("Sheld Damage Reduction Change: 6000")
            print("Base Damage Change: 120 dmg/hit")
            print("A legendary artifact that was claimed to have been banished and")
            print("banned by the intergalactic federation for its inconceivable power")
            print(", this one seems a little worn out though.")
            while equip == "NAN":
                equip=input("Equip it? [X] No thank you [Y]")
                if equip == "X":
                    OriP1Wea=120
                    ShldBlok = 6000
                    UnivEnWea = 1
                    equip = "NAN"
                    basicweapon = "Uno Reverse Card"
                    game()
                elif equip == "Y":
                    print("You discarded the weapon reluctantly onto the mold infested ground.")
                    equip = "NAN"
                    game()
                else:
                    print("Invalid Response")
                    equip = "NAN"
    else:
        print("Sadly, no weapon was found.")
                
            
            
def randomencount():
    chance=randint(1,3)
    if chance== 1:
        game()
    elif chance == 2:
        randomeny()
    else:
        print("HI")

def stats():
    print("|-----------Current Stats-----------|")
    print("|<",Name,">|")
    print("|Atk Damage:",OriP1Wea,"|")
    print("|Weapon:",basicweapon,"|")
    print("|Defence:",ShldBlok,"|")
    print("|HP:",P1HP,"|")
    print("|-----------------------------------|")
    Stat = "Open"
    while Stat == "Open":
        Stat=input("Close Stats? [s]")
        if Stat == "s":
            Stat = "Close"
        else:
            print("<SYSTEM> Invalid Response")
            Stat = "Open"
    
        
def fightscreen():
    global EnHP
    global PlHP
    if Enem == "Wombie":
        print("|-----------------------------------|")
        print("|  <",Name,">          <",Enem,">   |")
        print("|--<",P1HP,"HP>--------<",EnHP,"HP>-|")
        print("|------o--/--------------\--o-------|")
        print("|----(-|-/----------------\-|-)-----|")
        print("|-----/-\------------------/-\------|")
        time.sleep (0.3)
        print("|--Atk[X] Heal[Y] Shld[Z] Flee[A]---|")
    elif Enem == "Beegrock":
        print("|-----------------------------------|")
        print("|  <",Name,">          <",Enem,">   |")
        print("|--<",P1HP,"HP>--------<",EnHP,"HP>-|")
        print("|------o--/------------\--ooo-------|")
        print("|----(-|-/--------------\o.o.o------|")
        print("|-----/-\-----------------ooo-------|")
        time.sleep (0.3)
        print("|--Atk[X] Heal[Y] Shld[Z] Flee[A]---|")
    elif Enem == "A":
        print("|-----------------------------------|")
        print("|  <",Name,">          <",Enem,">   |")
        print("|--<",P1HP,"HP>--------<",EnHP,"HP>-|")
        print("|------o--/---------------/\--------|")
        print("|----(-|-/---------------/__\-------|")
        print("|-----/-\---------------/....\------|")
        time.sleep (0.3)
        print("|--Atk[X] Heal[Y] Shld[Z] Flee[A]---|")
    else:
        print("Bad Guy")
    
def fight():
    global UnivEnWea
    global EnHP
    global P1HP
    global ShldBlok
    global ShldBlokEn
    global Enem
    global applecount
    global enemyheal
    global healcounten
    global appleget
    while EnHP>0 and P1HP>0:
        P1turn="true"
        EnWea=OriEnWea
        P1Wea=OriP1Wea
        flee=0
        fightscreen()
        P1="0"
        E1="0"
        while P1turn=="true":
            P1=input("Make your move.")
            if P1=="X":
                EnHP=EnHP-P1Wea
                print("<",Name,">You have dealt",P1Wea,"damage!!")
                P1turn="false"
            elif P1=="Y":
                if applecount>0:
                    P1HP=P1HP+25
                    applecount=applecount-1
                    print("You used 1 apple!")
                    time.sleep(1)
                    print("<",Name,">You recovered 25 HP!!")
                    P1turn="false"
                else:
                    print("<",Name,">You have no apples left!")
            elif P1=="Z":
                if EnWea <= 0:
                    print("<",Name,"> You have blocked",ShldBlok," damage!!")
                    P1turn="false"
                elif EnWea <= ShldBlok:
                    print("<",Name,"> You have blocked",ShldBlok," damage!!")
                    EnWea = 0
                    P1turn="false"
                else:
                    EnWea=EnWea-ShldBlok
                    print("<",Name,"> You have blocked",ShldBlok," damage!!")
                    P1turn="false"
            elif P1=="A":
                flee=randint(1,2)
                if flee == 1:
                    print("You have fleed sucessfully")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    game()
                else:
                    print("Unfortunately, you can't flee")
                    P1turn="false"
            else:
                print("Invalid Response")
        P1Wea=OriP1Wea

        while P1turn=="false":
            E1=randint(1,4)
            if E1==1:
                P1HP=P1HP-EnWea
                print("<Enemy> He has dealt",EnWea,"damage!!")
                P1turn="true"
            elif E1==2:
                if enemyheal>0:
                    EnHP=EnHP+healcounten
                    enemyheal=enemyheal-1
                    print("<Enemy> He recovered",healcounten,"HP!!")
                    P1turn="true"
            elif E1==3:
                if P1=="X":
                    if P1Wea<=0:
                        print("<Enemy> He has blocked",ShldBlokEn," damage!!")
                        P1turn="true"
                    elif P1Wea <= ShldBlokEn:
                        print("<Enemy> He has blocked",ShldBlokEn," damage!!")
                        EnWea = 0
                        P1turn="true"
                    else:
                        EnHP=EnHP+ShldBlokEn
                        print("<Enemy> He has blocked",ShldBlokEn," damage!!")
                        P1turn="true"
                
            else:
                print("The enemy was thinking so hard that he has forgotten what was he doing!")
                P1turn="true"
        EnWea=OriEnWea
    if EnHP<=0:
        print("You have defeated",Enem,"!!")
        appleget = randint(1,4)
        applecount = applecount + appleget
        time.sleep(1)
        if appleget == 1:
            print("You have obtained",appleget,"apple!")
        else:
            print("You have obtained",appleget,"apples!")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        game()
    else:
        playerdeath()
                
def playerdeath():
    print("|-----------------------------------|")
    time.sleep (0.3)
    print("|OOF OOF OOF OOF OOF OOF OOF OOF OOF|")
    time.sleep (0.3)
    print("|--------- You have died!-----------|")
    time.sleep (0.3)
    print("|----Try Again?(Title screen[X])----|")
    time.sleep (0.3)
    print("|----Restart From Last Save[Y]------|")
    time.sleep (0.3)
    print("|OOF OOF OOF OOF OOF OOF OOF OOF OOF|")
    time.sleep (0.3)
    diedie = "Yes"
    while diedie == "Yes":
        diedie=input("Make your choice")
        if diedie == "X":
            diedie = "No"
            startingscreen()
        elif diedie == "Y":
            diedie = "No"
            game()
        else:
            print("<SYSTEM> Invalid Response")
            diedie = "Yes"

def mappinterface():
    global savefile
    if savefile == 0:
        lines = ["|-----------------------------------| Map Legend:",
         "|---------....|----...-----n--------| | and - = Walls",
         "|-----------|.|--...|.......--------| * = Secret",
         "|---@.....|-|.|--.|-@--|.||..|------| @ = Boss- You need to defeat them to",
         "|-------|.|-|.|--.|-.--|.||-........|           obtain a key fragment.",
         "|-------|............---....------|.| n = A door",
         "|-----------------------------------| X = Your current location"]

        for line in lines:         
            for c in line:         
                print(c, end='')   
                sys.stdout.flush()
                time.sleep(0.02)
            print('')
        time.sleep(2)
#        print("|-----------------------------------| Map Legend:")
 #       time.sleep (0.3)
#       print("|---------....|----...-----n--------| | and - = Walls")
 #       time.sleep (0.3)
#       print("|-----------|.|--...|.......--------| * = Secret")
 #       time.sleep (0.3)
 #       print("|---@.....|-|.|--.|-@--|.||..|------| @ = Boss- You need to defeat them to")
 #       time.sleep (0.3)
 #       print("|-------|.|-|.|--.|-.--|.||-........|           obtain a key fragment.")
 #       time.sleep (0.3)
 #       print("|-------|............---....------|.| n = A door")
 #       time.sleep (0.3)
 #       print("|-----------------------------------| X = Your current location")
 #       time.sleep (0.3)
    elif savefile == 1:
        print("|-----------------------------------| Map Legend:")
        print("|---------....|----...-----n--------| | and - = Walls")
        print("|-----------|.|--...|.......--------| * = Secret")
        print("|---@.....|-|.|--.|-@--|.||..|------| @ = Boss- You need to defeat them to")
        print("|-------|.|-|.|--.|-.--|.||-........|           obtain a key fragment.")
        print("|-------|............---....------|X| n = A door")
        print("|-----------------------------------| X = Your current location")
    elif savefile == 2:
        print("|-----------------------------------| Map Legend:")
        print("|---------....|----...-----n--------| | and - = Walls")
        print("|-----------|.|--...|.......--------| * = Secret")
        print("|---@.....|-|.|--.|-@--|.||..|------| @ = Boss- You need to defeat them to")
        print("|-------|.|-|.|--.|-.--|.||-........|           obtain a key fragment.")
        print("|-------|............---....------|X| n = A door")
        print("|-----------------------------------| X = Your current location")
    elif savefile == 3:
        print("|-----------------------------------| Map Legend:")
        print("|---------....|----...-----n--------| | and - = Walls")
        print("|-----------|.|--...|.......--------| * = Secret")
        print("|---@.....|-|.|--.|-@--|.||..|------| @ = Boss- You need to defeat them to")
        print("|-------|.|-|.|--.|-.--|.||-.......X|           obtain a key fragment.")
        print("|-------|............---....------|.| n = A door")
        print("|-----------------------------------| X = Your current location")
    elif savefile == 4:
        print("|-----------------------------------| Map Legend:")
        print("|---------....|----...-----n--------| | and - = Walls")
        print("|-----------|.|--...|.......--------| * = Secret")
        print("|---@.....|-|.|--.|-@--|.||..|------| @ = Boss- You need to defeat them to")
        print("|-------|.|-|.|--.|-.--|.||-......X.|           obtain a key fragment.")
        print("|-------|............---....------|.| n = A door")
        print("|-----------------------------------| X = Your current location")
    elif savefile == 5:
        print("|-----------------------------------| Map Legend:")
        print("|---------....|----...-----n--------| | and - = Walls")
        print("|-----------|.|--...|.......--------| * = Secret")
        print("|---@.....|-|.|--.|-@--|.||..|------| @ = Boss- You need to defeat them to")
        print("|-------|.|-|.|--.|-.--|.||-......X.|           obtain a key fragment.")
        print("|-------|............---....------|.| n = A door")
        print("|-----------------------------------| X = Your current location")
    elif savefile == 6:
        print("|-----------------------------------| Map Legend:")
        print("|---------....|----...-----n--------| | and - = Walls")
        print("|-----------|.|--...|.......--------| * = Secret")
        print("|---@.....|-|.|--.|-@--|.||..|------| @ = Boss- You need to defeat them to")
        print("|-------|.|-|.|--.|-.--|.||-.....X..|           obtain a key fragment.")
        print("|-------|............---....------|.| n = A door")
        print("|-----------------------------------| X = Your current location")
    elif savefile == 7:
        print("|-----------------------------------| Map Legend:")
        print("|---------....|----...-----n--------| | and - = Walls")
        print("|-----------|.|--...|.......--------| * = Secret")
        print("|---@.....|-|.|--.|-@--|.||..|------| @ = Boss- You need to defeat them to")
        print("|-------|.|-|.|--.|-.--|.||-.....X..|           obtain a key fragment.")
        print("|-------|............---....------|.| n = A door")
        print("|-----------------------------------| X = Your current location")
    elif savefile == 8:
        print("|-----------------------------------| Map Legend:")
        print("|---------....|----...-----n--------| | and - = Walls")
        print("|-----------|.|--...|.......--------| * = Secret")
        print("|---@.....|-|.|--.|-@--|.||..|------| @ = Boss- You need to defeat them to")
        print("|-------|.|-|.|--.|-.--|.||-....X...|           obtain a key fragment.")
        print("|-------|............---....------|.| n = A door")
        print("|-----------------------------------| X = Your current location")
    elif savefile == 9:
        print("|-----------------------------------| Map Legend:")
        print("|---------....|----...-----n--------| | and - = Walls")
        print("|-----------|.|--...|.......--------| * = Secret")
        print("|---@.....|-|.|--.|-@--|.||..|------| @ = Boss- You need to defeat them to")
        print("|-------|.|-|.|--.|-.--|.||-....X...|           obtain a key fragment.")
        print("|-------|............---....------|.| n = A door")
        print("|-----------------------------------| X = Your current location")


    
def mapp():
    mappinterface()
    time.sleep(0.3)
    
def compselect():
    compsel=input("Press E to initiate your inventory, Press S to view your current stats, Press M to view the map and Press G for the Menu")
    if compsel==E:
        inve()
    elif compsel==S:
        print("Enter Stat")
    elif compsel==M:
        mapp()
    elif compsel==G:
        print("Thong")
    else:
        print("Invalid Response")
        
def inve():
    global Otheritem
    global Otheritem2
    global Otheritem3
    inventory="open"
    inv= ["Apples","Map","Utility Tool",Otheritem,Otheritem2,Otheritem3]
    print("Inventory : ")
    print("o",inv[0],applecount)
    time.sleep (0.1)
    print("o",inv[1])
    time.sleep (0.1)
    print("o",inv[2])
    time.sleep (0.1)
    print("o",inv[3])
    time.sleep (0.1)
    print("o",inv[4])
    time.sleep (0.1)
    print("o",inv[5])
    while inventory == "open":
        x=input("Close Inventory? [i]")
        if x=="i":
            inventory="close"
        else:
            print("Invalid Response")
            inventory = "open"
    
def game():
    global savefile
    global direction
    global basicweapon
    global OriP1Wea
    global savefileuni
    global equip
    if savefile == 0:
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
        mapp()
        time.sleep(2)
        print("These are your personal statistics[Toggle it with the enter of a lowercase s]")
        time.sleep(2)
        stats()
        print("Let's Goo!!")
        savefile = 1
        game()
    elif savefile == 1:
        time.sleep (2)
        print(">You have set your first foot into the thick shrubs of the unnammed woodlands, oblivious of the creatures and dangers lurking inside...")
        time.sleep (3)
        print(">To navigate this treacherous forest, you must first understand the uses of the commands North(N), South(S), East(E)and West(W).")
        time.sleep (3)
        print(">The dialogue would usually tell you what are the availiable options, but generally, N=Up on the map, S=Down on the map, E=Right on the map and W=Left on the map")
        savefile = 2
        game()
        time.sleep (2)
    elif savefile == 2:
        mapp()
        print(">You can only move north from here. [N] [i] [s]")
        while direction == "NAN":
            direction=input("Make your move->")
            if direction == "N":
                savefile = 3
                direction = "NAN"
                game()
            elif direction == "s":
                stats()
                direction = "NAN"
            elif direction == "i":
                inve()
                direction = "NAN"
            else:
                direction = "NAN"
                print("Invalid Response")
    elif savefile == 3:
        if savefileuni == 0:
            mapp()
            print(">Your first step into the forest guides you along a path of sticks.")
            time.sleep(2)
            print(">A thick overgrown shrub covered in poisonous thorns sits in front of you, restricting your path.")
            time.sleep(2)
            savefileuni = 1
        else:
            mapp()
        print(">You can either move west or return. [W] [S] [i] [s]")
        while direction == "NAN":
            direction=input("Make your move->")
            if direction == "W":
                if savefileuni == 1:
                    savefile = 4
                    direction = "NAN"
                    game()
                elif savefileuni >= 2:
                    savefile = 5
                    direction = "NAN"
                    game()
            elif direction == "s":
                stats()
                direction = "NAN"
            elif direction == "i":
                inve()
                direction = "NAN"
            elif direction == "S":
                savefile = 2
                direction = "NAN"
                game()
            else:
                direction = "NAN"
                print("Invalid Response")
    elif savefile == 4:
        mapp()
        print(">You took a sharp left turn, placing yourself in a never ending pathway, where trees are situated in such an orderly fashion that you could reach the other side without making any turns.")
        time.sleep(10)
        print(">You examined your surroundings, something feels off, then a silhouette appears in front of you...")
        time.sleep(2)
        savefile = 5
        savefileuni = 2
        randomeny()
    elif savefile == 5:
        mapp()
        print(">You can either move west or return. [W] [E] [i] [s]")
        while direction == "NAN":
            direction=input("Make your move->")
            if direction == "W":
                if savefileuni == 2:
                    savefile = 6
                    direction = "NAN"
                    game()
                elif savefileuni >= 3:
                    savefile = 7
                    direction = "NAN"
                    game()
            elif direction == "s":
                stats()
                direction = "NAN"
            elif direction == "i":
                inve()
                direction = "NAN"
            elif direction == "E":
                savefile = 3
                direction = "NAN"
                game()
            else:
                direction = "NAN"
                print("Invalid Response")
    elif savefile == 6:
        mapp()
        print(">The pathway seemed longer than you have thought, I mean its not like the map is lying to you right?")
        time.sleep(4)
        print(">You have picked up what is known to be one of your first weapon, to obviously defend yourself in an enemy infested forest.")
        time.sleep(4)
        print("[Wooden Stick]")
        print("Atk damage = 10")
        print("Desc:")
        print("I know this is barely a weapon, but at least it could acheive")
        print("more successful things in life once by supporting a tree, unlike")
        print("you, continuously playing games all day :>.")
        while equip == "NAN":
                equip=input("Equip it? [X] No thank you [Y]")
                if equip == "X":
                    OriP1Wea = 10
                    ShldBlok = 2
                    UnivEnWea = 0
                    print("You have equiped the wooden stick.")
                    basicweapon = "Wooden Stick"
                elif equip == "Y":
                    print("You discarded the weapon, because your too strong for it.")
                else:
                    print("Invalid Response")
                    equip = "NAN"
        savefile = 7
        savefileuni=3
        randomencount()
        game()
    elif savefile == 7:
        mapp()
        print(">You can either move west or return. [W] [E] [i] [s]")
        while direction == "NAN":
            direction=input("Make your move->")
            if direction == "W":
                if savefileuni == 3:
                    savefile = 8
                    direction = "NAN"
                    game()
                elif savefileuni >= 4:
                    savefile = 9
                    direction = "NAN"
                    game()
                
            elif direction == "s":
                stats()
                direction = "NAN"
            elif direction == "i":
                inve()
                direction = "NAN"
            elif direction == "E":
                savefile = 5
                direction = "NAN"
                game()
            else:
                direction = "NAN"
                print("Invalid Response")

    elif savefile == 8:
        mapp()
        print(">You walked further into the overgrown landscape, it seems as if youare half way through the pathway!")
        time.sleep(4)
        print(">This forest seemed rather different, the enemies look like otherworldly lifeforms that has just freshly entered earth.")
        time.sleep(4)
        print(">You ignored your thoughts, just to let your mind calm down. [Aliens?] Pfffft There is currently no evidence that proves that they exist.")
        savefile = 9
        savefileuni = 4
        randomencount()
        game()
    elif savefile == 9:
        mapp()
        print(">You can either move west or return. [W] [E] [i] [s]")
        while direction == "NAN":
            direction=input("Make your move->")
            if direction == "W":
                savefile = 10
                direction = "NAN"
                game()
            elif direction == "s":
                stats()
                direction = "NAN"
            elif direction == "i":
                inve()
                direction = "NAN"
            elif direction == "E":
                savefile = 7
                direction = "NAN"
                game()
            else:
                direction = "NAN"
                print("Invalid Response")
            

def cred():
    print("|--------Special Thanks to:---------|")
    time.sleep (1)
    print("|-----Game Developer - Yee Zhen-----|")
    time.sleep (1)
    print("|------Game Designer - Yee Zhen-----|")
    time.sleep (1)
    print("|------Game Planner - Yee Zhen------|")
    time.sleep (1)
    print("|--Here is a random peice of text---|")
    time.sleep (1)
    print("|-----------------------------------|")
    time.sleep (2)
    startingscreen()
    
def startingscreen():
    print("|-----------------------------------|")
    time.sleep (0.1)
    print("|----------Adventure Game-----------|")
    time.sleep (0.1)
    print("|----------Play [Press X]-----------|")
    time.sleep (0.1)
    print("|------Instructions [Press Y]-------|")
    time.sleep (0.1)
    print("|---------Credits [Press T]---------|")
    time.sleep (0.1)
    print("|-----------------------------------|")
    time.sleep (0.5)
    cmd="NAN"
    while cmd=="NAN":
        cmd=input("<SYSTEM> Awaiting Commands...")
        if cmd == "X":
            game()
            
        elif cmd == "Y":
            ins()
            
        elif cmd == "T":
            cred()

        elif cmd == "x":
            randomeny()
            
        elif cmd == "y":
            while ultimateweapon == 0:
                randomloot()
            

        elif cmd == "t":
            cred()
            
        elif cmd == "6969":
            Easteregg=0
            print("Secret found")
            Easteregg=Easteregg+1
            print("Total secrets found:",Easteregg,"/5")
            cmd = "NAN"
            
        else:
            print("<SYSTEM> Invalid Response")
            cmd = "NAN"
def ins():
    print("|----------------------------------------------------------|")
    time.sleep (0.1)
    print("|-----------------------Instructions-----------------------|")
    time.sleep (0.1)
    print("|Please enter all of your text as displayed by the screens.|")
    time.sleep (0.1)
    print("|-------------------(This includes caps)-------------------|")
    time.sleep (0.1)
    print("|-------------------And also, have fun!!-------------------|")
    time.sleep (0.1)
    print("|-----------------------Got it [x]-------------------------|")
    time.sleep (0.1)
    print("|----------------------------------------------------------|")
    Instruct = "NAN"
    while Instruct == "NAN":
        Instruct=input("<SYSTEM> Awaiting Commands...")
        if Instruct == "x":
            startingscreen()
        else:
            print("<SYSTEM> Invalid Response")
            Instruct = "NAN"

def variable():
    ShldBlok=2
    ShldBlokEn=1
    Enem = "Bad Guy"
    OriP1Wea=5
    OriEnWea=5
    P1Wea=OriP1Wea
    EnWea=OriEnWea
    OriP1HP=100
    OriEnHP=100
    UnivEnWea=1
    P1HP=OriP1HP
    EnHP=OriEnHP
    applecount = 3
    oricount = 3
    enemyheal = oricount
    healcounten = 5
    Otheritem="-"
    Otheritem2="-"
    Otheritem3="-"
    ultimateweapon = 0
    equip = "NAN"
    loot = 0
    appleget = 0
    basicweapon = "Noodle Arms"
    savefile=0
    savefileuni=0
    direction="NAN"
    Name = 0
    Age = 0
    Easteregg=0
    with open('savefile.dat', 'wb') as NameSave:
        pickle.dump([Name], NameSave, protocol=2)
    
import pickle
user_savedata_game=(2,1,"Bad Guy",5,5,100,100,1)
ShldBlok=user_savedata_game[0]
ShldBlokEn=user_savedata_game[1]
Enem = user_savedata_game[2]
OriP1Wea=user_savedata_game[3]
OriEnWea=user_savedata_game[4]
P1Wea=OriP1Wea
EnWea=OriEnWea
OriP1HP=user_savedata_game[5]
OriEnHP=user_savedata_game[6]
UnivEnWea=user_savedata_game[7]
P1HP=OriP1HP
EnHP=OriEnHP
applecount = 3 
oricount = 3
enemyheal = oricount
healcounten = 5
Otheritem="-"
Otheritem2="-"
Otheritem3="-"
ultimateweapon = 0
equip = "NAN"
loot = 0
appleget = 0
basicweapon = "Noodle Arms"
savefile=0
savefileuni=0
direction="NAN"
Easteregg=0
TimesEntered = 1
import time
from random import randint
from time import sleep
from random import uniform
import sys
filename = 'USER_SAVEDATA_2020_EXTERIOR_FILE'

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




