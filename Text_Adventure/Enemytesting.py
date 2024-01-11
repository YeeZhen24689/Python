from random import randint
from random import random
import time
import os

clear = lambda : os.system('cls')

class WeaponC:

    weaponname = { 
                   1: {'Name':'Sword','BaseDmg':15,'Attackup':'Wombie','Weight':1,'Atkfreq':1,'Turnfall':1}, # Atk once a turn, standard dmg.
                   2: {'Name':'Crossbow','BaseDmg':20,'Attackup':'Hellicopeter','Weight':1,'Atkfreq':1,'Turnfall':1}, # Atk once every two turns, twice dmg.
                   3: {'Name':'Claymore','BaseDmg':25,'Attackup':'Golem','Weight':2,'Atkfreq':1,'Turnfall':1}, # Atk immediately with huge dmg, following a two turn stagger and recoil.
                   4: {'Name':'Set of Gauntlets','BaseDmg':9,'Attackup':'Slime','Weight':0,'Atkfreq':0.5,'Turnfall':0.5}, # Atk twice a turn, half std dmg.
                   5: {'Name':'Syche','BaseDmg':23,'Attackup':'No','Weight':1,'Atkfreq':1,'Turnfall':1}, # Atk like sword, 5% chance to deal twice dmg.
                 }

    def __init__(self,storystate) -> None:

        weapondmg = randint(80,110)
        weaponrand = randint(1,5)
        self.name = self.weaponname[weaponrand]['Name']
        self.dmg =  round(self.weaponname[weaponrand]['BaseDmg'] * (storystate/7)*(weapondmg/100),0)+1 
        self.Attackup = '+' + str(storystate) + ' damage to ' + self.weaponname[weaponrand]['Attackup']
        self.Attackupval = self.weaponname[weaponrand]['Attackup']
        self.Weight = self.weaponname[weaponrand]['Weight']
        self.atk_frequency = self.weaponname[weaponrand]['Atkfreq']
        self.turnfall = self.weaponname[weaponrand]['Turnfall']

class InventoryC:

    def __init__(self):
        self.store = []           #stores the names of the items (derived from class)
        self.quantity = []        #stores the quantity of each individual item (derived from class)
        self.storeAttribute = []  #stores the item class
        self.storeType = []       #stores the type of item
        self.index = []           #stores an external index reference so it makes calling each item easier
        self.capacity = 10        #player storage capacity

    def additem(self,item):
        old = self.store
        Ichangedthequantity=0
        for i in old:
            if sum(self.quantity) >= self.capacity:
                cho = input('There are too many things in your bag to hold this, throw something away? [y] [n]')
                if cho == 'y':
                    self.destroyitem(item)
                elif cho == 'n':
                    return self
            else:
                if i == item.name:
                    self.quantity[self.store.index(i)]+=1
                    Ichangedthequantity=1
                else:
                    pass

        if self.store == []:
            self.itemappend(item)
        elif Ichangedthequantity==0:
            self.itemappend(item)
        return self
   
    def itemappend(self,item):
        self.index.append(len(self.store))
        self.store.append(item.name)
        self.storeAttribute.append(item)
        self.quantity.append(1)
        self.storeType.append(item.type)

    def destroyitem(self,index):
        #show inventory
        if index == -1:
            cho = int(input('What do you want to get rid of? [Type index number]'))
        else:
            cho = index
        
        if cho < self.capacity and cho > -1:
            if self.quantity[cho] > 1:
                self.quantity[cho] -= 1
            
            elif self.quantity[cho] == 1:
                del self.store[cho]
                del self.storeAttribute[cho]
                del self.quantity[cho]
        else:
            print('That location does not exist in your bag.')
            self.destroyitem(index)

        return self
    
    def useinventoryitem(self,player):

        if len(self.storeAttribute) == 0:
            print("There is nothing in your bag.")
            return player

        choice = input("Use something? (Enter Valid Index) or Return (r) -> ")
        if choice < str(len(self.storeAttribute)) and choice > "-1":
            choice = int(choice)
            typeofitem = self.storeAttribute[choice].type
            if typeofitem == "Healing Item": #Heals the player
                player.hp = round(player.hp + self.storeAttribute[choice].healing,1)
                print(self.index[choice])
                self.destroyitem(self.index[choice]) 
                return player
            
            elif typeofitem == "Story Item": #Makes sure item is not story item
                print("This item cannot be used.")
                return player

            elif typeofitem == "Supplement Item": #Def + Attack Boost
                if self.storeAttribute[choice].name == 'X Attack':
                    #powerup function
                    pass
                elif self.storeAttribute[choice].name == 'X Defence':
                    #powerup function
                    pass
            
            else:
                pass
        elif choice == 'r':
            pass
        else:
            print("That is not a valid option")
        return player
 
class ItemC:

    itemname = { 
                   1: {'Name':'Key Fragment','Healing':0,'Type':'Story Item','Attackup':0,'Defenceup':0,'Usable':0},
                   2: {'Name':'Battery','Healing':20,'Type':'Healing Item','Attackup':5,'Defenceup':0,'Usable':1}, # Atk once a turn, standard dmg.
                   3: {'Name':'Scrap','Healing':30,'Type':'Healing Item','Attackup':0,'Defenceup':2,'Usable':1}, # Atk once every two turns, twice dmg.
                   4: {'Name':'X Attack','Healing':0,'Type':'Supplement Item','Attackup':10,'Defenceup':0,'Usable':1}, # Atk twice a turn, half std dmg.
                   5: {'Name':'X Defence','Healing':0,'Type':'Supplement Item','Attackup':0,'Defenceup':20,'Usable':1}, # Atk like sword, 5% chance to deal twice dmg.
                }

    def __init__(self,storystate):

        item = randint(0,100)
        if item == 99:
            item = randint(4,5)
        else:
            item = randint(2,3)

        self.name = self.itemname[item]['Name']
        self.healing = self.itemname[item]['Healing']*(storystate/7)
        self.type = self.itemname[item]['Type']
        self.attackup = self.itemname[item]['Attackup']
        self.defenceup = self.itemname[item]['Defenceup']
        self.usable = self.itemname[item]['Usable']

    def reset(self,storystate):

        item = randint(0,100)
        if item == 99:
            item = randint(4,5)
        else:
            item = randint(2,3)

        self.name = self.itemname[item]['Name']
        self.healing = self.itemname[item]['Healing']*(storystate/7)
        self.type = self.itemname[item]['Type']
        self.attackup = self.itemname[item]['Attackup']
        self.Weight = self.itemname[item]['Weight']
        self.usable = self.itemname[item]['Usable']

class PlayerC:

    maxhp = 100

    def __init__(self,name,weapon,storystate) -> None:

        self.name = name
        self.hp = self.recov2fullhp(storystate)
        self.atk = 10 + weapon.dmg
    
    def recov2fullhp(self,storystate):
        if storystate < 4:
            hp = self.maxhp*.5
            self.inventorymax = 5
        elif storystate == 5 or storystate == 6:
            hp = self.maxhp*.75
            self.inventorymax = 10
        else:
            hp = self.maxhp
            self.inventorymax = 15
        return hp     

    def playerturn(self,enemy,weapon,storystate):
 
        if enemy.name == weapon.Attackupval:
            factor = storystate
        else:
            factor = 0

        enemy.hp = round(enemy.hp - (weapon.dmg + factor),0)
        print(f'You have dealt {weapon.dmg + factor} damage.')
        return enemy
        
    def enemyturn(self,enemy):

        self.hp = self.hp-enemy.atk
        print(f'The enemy has dealt {enemy.atk} damage.')
        return self

class EnemyC:
    
    Enemystat = {
                 1: {'name': 'Golem', 'bhp': 75, 'ba': 20, 'Weight': 1, 'Turnfall':1.1, 'Recovery':0.1, 'Healcount':2, 'Fleechance':1},
                 2: {'name': 'Wombie', 'bhp': 30, 'ba': 25, 'Weight': 1,'Turnfall':0.51, 'Recovery':0.2, 'Healcount':3, 'Fleechance':.5 },
                 3: {'name': 'Slime', 'bhp': 18, 'ba': 10, 'Weight': 1,'Turnfall':0.21, 'Recovery':0.1, 'Healcount':10, 'Fleechance':.5 },
                 4: {'name': 'Hellicopeter', 'bhp': 50, 'ba': 30, 'Weight': 2,'Turnfall':1.1, 'Recovery':0.4, 'Healcount':2, 'Fleechance':.1 },
                 }

    def __init__(self,storystate):

        randomenemy=randint(1,4)
        print(randomenemy)
        randomiserha = randint(90,120)
        randomability=randint(1,5)
        if randomability == 5:
            Strongerscaling=1.5
        else:
            Strongerscaling=1
        self.name=self.Enemystat[randomenemy]['name']
        self.maxhp=round(Strongerscaling*self.Enemystat[randomenemy]['bhp']*(randomiserha/100)*(storystate/7),0)
        self.hp=round(Strongerscaling*self.Enemystat[randomenemy]['bhp']*(randomiserha/100)*(storystate/7),0)
        self.atk=round(Strongerscaling*self.Enemystat[randomenemy]['ba']/(randomiserha/100)*(storystate/7),0)
        self.recov=self.Enemystat[randomenemy]['bhp']*self.Enemystat[randomenemy]['Recovery']
        self.Weight=self.Enemystat[randomenemy]['Weight']
        self.healcount=self.Enemystat[randomenemy]['Healcount'] #Times it can heal a turn
        self.turnfall=self.Enemystat[randomenemy]['Turnfall']
        self.decisionrecall=0
        self.fleechance=self.Enemystat[randomenemy]['Fleechance']

    def atkread(self):

        strcount=self.name 
        linecounter=0
        savestatecount=0
        file = open('EnemyData.txt', 'r') # Calls the file we are specifying

        for lines in file: 
            editlines=lines.replace("\n","") # We want to get rid of \n to clean up the output, no spaces between lines.
            numend="End"+strcount # End1, End2 in txt file
            if editlines == numend:
                savestatecount=0
            elif savestatecount == 1:
                linecounter+=1
                if linecounter == 9:
                    editlines=editlines.replace("X","_",int(round((1-(self.hp/self.maxhp))*18,0))) #Healthbar
                    print(editlines)
                else:
                    print(editlines)
            else:
                pass
            
            if editlines == strcount: 
                savestatecount=1
                
        file.close()

    def heal(self):
        if self.healcount > 0:
            healed = True
            if self.hp + self.recov < self.maxhp:
                self.hp += self.recov
            else:
                self.hp = self.maxhp
            self.healcount -= 1
            print(f'The enemy has healed for {self.recov} hitpoints.')
        
        else:
            healed = False

        return healed

    def Decision(self,weapon):
        recklessness = randint(0,1)
        if self.decisionrecall == 0 or self.healcount > 0:
            if recklessness == 0: # Not Reckless
                if self.hp < self.maxhp*0.5:
                    return 'heal'
                else:
                    return 'attack'
            elif recklessness == 1: # Not Reckless
                if self.hp < weapon.dmg:
                    return 'heal'
                else:
                    return 'attack'
        else:
            return 'attack'
        print("IDK Bro")
                    
class BossC:
    
    Bossstat = { 1: {'name': 'The Undead Golaith', 'bhp': 50, 'ba': 20, 'Weight': 1, 'Turnfall':1.1, 'Recovery':0.1,'Phase':2, 'Healcount':2, 'Fleechance':1},
                 2: {'name': 'The Forest Guardian', 'bhp': 100, 'ba': 25, 'Weight': 1,'Turnfall':0.51, 'Recovery':0.4,'Phase':3, 'Healcount':3, 'Fleechance':.5 },
                 3: {'name': 'The Grand Slime', 'bhp': 100, 'ba': 10, 'Weight': 1,'Turnfall':0.51, 'Recovery':0.5,'Phase':2, 'Healcount':10, 'Fleechance':.5 },
                 4: {'name': 'The Stargazer', 'bhp': 100, 'ba': 30, 'Weight': 2,'Turnfall':1.1, 'Recovery':0.1,'Phase':4, 'Healcount':2, 'Fleechance':.1 },
                 }

    def __init__(self,boss):

        self.name=self.Bossstat[boss]['name']
        self.maxhp=round(self.Bossstat[boss]['bhp'],0)
        self.hp=round(self.Bossstat[boss]['bhp'],0)
        self.atk=round(self.Bossstat[boss]['ba'],0)
        self.recov=self.Bossstat[boss]['bhp']*self.Bossstat[boss]['Recovery']
        self.Weight=self.Bossstat[boss]['Weight']
        self.healcount=self.Bossstat[boss]['Healcount'] #Times it can heal a turn
        self.turnfall=self.Bossstat[boss]['Turnfall']
        self.phase=self.Bossstat[boss]['Phase']
        self.decisionrecall=0

    def reset(self,boss):

        self.name=self.Bossstat[boss]['name']
        self.maxhp=round(self.Bossstat[boss]['bhp'],0)
        self.hp=round(self.Bossstat[boss]['bhp'],0)
        self.atk=round(self.Bossstat[boss]['ba'],0)
        self.recov=self.Bossstat[boss]['bhp']*self.Bossstat[boss]['Recovery']
        self.Weight=self.Bossstat[boss]['Weight']
        self.healcount=self.Bossstat[boss]['Healcount'] #Times it can heal a turn
        self.turnfall=self.Bossstat[boss]['Turnfall']
        self.phase=self.phase
        self.decisionrecall=0

    def dead(self,boss):
        if self.phase == 0:
            return self
        elif self.phase > 0:
            self = self.reset(self,boss)
            self.phase -= 1
            return self

    def heal(self):
        if self.healcount > 0:
            healed = True
            if self.hp + self.recov < self.maxhp:
                self.hp += self.recov
            else:
                self.hp = self.maxhp
            self.healcount -= 1
            print(f'The Boss has healed for {self.recov} hitpoints.')
        
        else:
            healed = False

        return healed

    def Decision(self,weapon):
        recklessness = randint(0,1)
        if self.decisionrecall == 0:
            if recklessness == 0: # Not Reckless
                if self.hp < self.maxhp*0.5:
                    return 'heal'
                else:
                    return 'attack'
            elif recklessness == 1: # Not Reckless
                if self.hp < weapon.dmg:
                    return 'heal'
                else:
                    return 'attack'
        else:
            return 'attack' 
        
    def atkread(self):
        strcount=self.name+str(self.phase)
        linecounter=0
        savestatecount=0
        file = open('EnemyData.txt', 'r') # Calls the file we are specifying

        for lines in file: 
            editlines=lines.strip # We want to get rid of \n to clean up the output, no spaces between lines.
            numend="End"+strcount # End1, End2 in txt file
            if editlines == numend:
                savestatecount=0
            elif savestatecount == 1:
                linecounter+=1
                if linecounter == 10:
                    editlines=editlines.replace("X","_",int(round((1-(self.hp/self.maxhp))*18,0))) #Healthbar
                    print(editlines)
                else:
                    print(editlines)
            else:
                pass
            
            if editlines == strcount: 
                savestatecount=1
                
        file.close()

def fightplayer(Weapon,Player,Enemy,Storystate,flee,Inventory):
    turncreditsp=1
    while turncreditsp > 0:
        choice = input(' |X|Attack  |Y|Check  |Z|Inv  |O|Run  ->')
        if choice == 'X':
            turncreditsp -= Weapon.atk_frequency
            Enemy = Player.playerturn(Enemy, Weapon, Storystate)
        elif choice == 'Y':
            UIread(Enemy)
        elif choice == 'Z':
            UIread(Inventory)
            Player=Inventory.useinventoryitem(Player)
        elif choice == 'O':
            if random() < Enemy.fleechance:
                turncreditsp -= 1
                flee = 1
            else:
                print('You failed to escape')
                turncreditsp -= 1
                pass
        print('|--------------------------------------|')

    return Enemy,flee

def fightenemy(Weapon,Player,Enemy):
    turncreditse=1
    while turncreditse > 0:
        decision = Enemy.Decision(Weapon)
        if Enemy.decisionrecall == 0:
            if decision == 'attack':
                turncreditse -= Enemy.turnfall
                Player = Player.enemyturn(Enemy)
            elif decision == 'heal':
                turncreditse -= Enemy.turnfall
                healed=Enemy.heal()
                if not healed: 
                    Enemy.decisionrecall=1
                else:
                    pass
        else:
            Player = Player.enemyturn(Enemy)
            turncreditse -= Enemy.turnfall
        time.sleep(1)

    return Player,Enemy

def checkWeight(Weapon,Player,Enemy,Storystate,flee,Inventory):
    
    if Weapon.Weight <= Enemy.Weight:
      # player go first
        Enemy,flee = fightplayer(Weapon,Player,Enemy,Storystate,flee,Inventory)
        if Enemy.hp < 0 or flee == 1:
            return Player,Enemy,flee
        Player,Enemy = fightenemy(Weapon,Player,Enemy)
        if Player.hp < 0:
            return Player,Enemy,flee
    else:
      # enemy go first
        Player,Enemy = fightenemy(Weapon,Player,Enemy)
        if Player.hp < 0:
            return Player,Enemy,flee
        Enemy,flee = fightplayer(Weapon,Player,Enemy,Storystate,flee,Inventory)
        if Enemy.hp < 0 or flee == 1:
            return Player,Enemy,flee

    return Player,Enemy,flee

def turn(Weapon,Player,Enemy,Storystate,Inventory):
    flee = 0
    while Player.hp > 0 and Enemy.hp > 0 and flee == 0:
        Enemy.decisionrecall=0

        clear()
        Enemy.atkread()
        print(f'     Your hp: {Player.hp} | Enemy hp: {Enemy.hp}')
        Player,Enemy,flee = checkWeight(Weapon,Player,Enemy,Storystate,flee,Inventory)
        input('Press enter to continue')

        if flee == 1:
            break

    return Player,Enemy,flee

def turnfall(Class):
    # A counter to determine the turns an enemy/weapon can attack a turn
    for i in range(10):
        if 1 - Class.turnfall*i < 0:
            Turns = i - 1
            break
        else: 
            pass
    return Turns

def UIread(Class):

    if Class.__class__.__name__ == 'WeaponC':
        strcount='Weapon'
    elif Class.__class__.__name__ == 'EnemyC':
        strcount='Check'
    elif Class.__class__.__name__ == 'InventoryC':
        strcount='Inventory'
    linecounter=0
    savestatecount=0
    file = open('UI.txt', 'r') # Calls the file we are specifying

    for lines in file: 
        editlines=lines.replace("\n","") # We want to get rid of \n to clean up the output, no spaces between lines.
        numend="End"+strcount # End1, End2 in txt file
        
        if editlines == numend:
            savestatecount=0
        
        elif savestatecount == 1:
            time.sleep(0.1)
            linecounter+=1
            if linecounter == 1 or linecounter == 8:
                editlines=editlines.replace("Weapon",Class.name)
            elif linecounter == 3:
                editlines = editlines + "     " +str(Class.dmg)
            elif linecounter == 4:
                editlines = editlines + "     " +str(Class.Weight)
            elif linecounter == 5:
                editlines = editlines + " " + Class.Attackup
            elif linecounter == 6:
                editlines = editlines + "     " +str(turnfall(Class))
            else:
                pass
            print(editlines)

        elif savestatecount == 2:
            
            time.sleep(0.1)
            linecounter+=1
            if linecounter == 2:
                editlines=editlines.replace("Enemy",Class.name)
            elif linecounter == 4:
                editlines = editlines + "             " +str(Class.atk)
            elif linecounter == 5:
                editlines = editlines + "             " +str(Class.hp)
            elif linecounter == 6:
                editlines = editlines + "             " +str(Class.Weight)
            elif linecounter == 7:
                editlines = editlines + "     " +str(turnfall(Class))
            else:
                pass
            print(editlines)

        elif savestatecount == 3: 
            time.sleep(0.1)
            linecounter+=1
            if linecounter == 3:
                print('      Amount     ID      Name     Type')
                for i in Class.index:
                    print(f'{Class.quantity[i]}  {i}  {Class.store[i]}  {Class.storeType[i]}')
            else:
                pass
            print(editlines)

        else:
            pass
        
        if editlines == strcount:
            if strcount == 'Weapon': 
                savestatecount=1
            elif strcount == 'Check':
                savestatecount=2
            elif strcount == 'Inventory':
                savestatecount=3
            
    file.close()
    return

def weaponroll(currentweapon,storystate):
    dm = 0 # Decision made
    Weaponnew=WeaponC(storystate)
    print(f'In the ashes, you find a {Weaponnew.name}!') 
    time.sleep(1)
    UIread(Weaponnew)

    while dm == 0: # When decision is not made.
        choice = input('Do you want to switch to this weapon? [Y] [N]')
        if choice == 'Y' or choice == 'N':
            dm = 1
        else:
            print('Invalid Response.')

    if choice == 'Y':
        return Weaponnew
    elif choice == 'N':
        return currentweapon

def battle(storystate,name,Inventory,Weapon):

    Player = PlayerC(name,Weapon,storystate)
    Item1 = ItemC(storystate)
    Item2 = ItemC(storystate)
    Enemy = EnemyC(storystate)
    Player,Enemy,flee = turn(Weapon,Player,Enemy,storystate,Inventory)

    if flee == 1:
        print('You got away successfully.')
    elif Player.hp > 0 and Enemy.hp < 0:
        print('Player wins')
        print(f'You obtained 1x {Item1.name}!')
        Inventory.additem(Item1)
        print(f'You obtained 1x {Item2.name}!')
        Inventory.additem(Item2)
        Weapon=weaponroll(Weapon,storystate)
    elif Player.hp < 0 and Enemy.hp > 0:
        print('Enemy wins')
    elif Player.hp < 0 and Enemy.hp < 0:
        print('No one won.')
    else:
        print('Debug Error')
    input('Press enter to continue')

    return Player,Weapon,Inventory

def Var_declaration():
    #Placed key variables in a function to allow the whole game to reset as well as saving.
    storystate=3
    pos=[4,36]
    return storystate, pos

def main():
    storystate,pos = Var_declaration()

    name = input('What is your name?')
    Inventory = InventoryC()
    Weapon = WeaponC(storystate)
    while True:
        Player, Weapon, Inventory = battle(storystate,name,Inventory,Weapon)
        print(Inventory.store)
        print(Inventory.quantity)
        input('next')

main()