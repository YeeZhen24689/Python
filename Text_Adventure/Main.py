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
                   6: {'Name':'Xcaliburr','BaseDmg':50,'Attackup':'No','Weight':1,'Atkfreq':0.2,'Turnfall':1}, # Atk like sword, 5% chance to deal twice dmg. 
                 }

    def __init__(self,Storystate) -> None:

        weapondmg = randint(80,110)
        weaponrand = randint(1,6)
        self.name = self.weaponname[weaponrand]['Name']
        self.dmg =  round(self.weaponname[weaponrand]['BaseDmg'] * (Storystate/7)*(weapondmg/100),0)+1 
        self.Attackup = '+' + str(Storystate) + ' damage to ' + self.weaponname[weaponrand]['Attackup']
        self.Attackupval = self.weaponname[weaponrand]['Attackup']
        self.Weight = self.weaponname[weaponrand]['Weight']
        self.atk_frequency = self.weaponname[weaponrand]['Atkfreq']
        self.turnfall = self.weaponname[weaponrand]['Turnfall']

class InventoryC:

    def __init__(self,Player):
        self.store = []           #stores the names of the items (derived from class)
        self.quantity = []        #stores the quantity of each individual item (derived from class)
        self.storeAttribute = []  #stores the item class
        self.storeType = []       #stores the type of item
        self.index = []           #stores an external index reference so it makes calling each item easier
        self.capacity = Player.inventorymax       #player storage capacity

    def additem(self,item):
        old = self.store
        Ichangedthequantity=0

        if sum(self.quantity) >= self.capacity:
            cho = input('There are too many things in your bag to hold this, throw something away? [y] [n]')
            if cho == 'y':
                self.destroyitem(-1)
            elif cho == 'n':
                return self
            else:
                self.additem(item)

        for i in old:
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

    def deletionfrominventory(self,index):
        if self.quantity[index] > 1:
            self.quantity[index] -= 1

        elif self.storeType[index] == 'Story Item':
            print("You cannot delete a story item.")
            return
                
        elif self.quantity[index] == 1:
            del self.index[len(self.index)-1]
            del self.store[index]
            del self.storeAttribute[index]
            del self.quantity[index]
        
        return

    def destroyitem(self,item):
        if item == -1:
            UIread(self)
            cho = int(input('What do you want to get rid of? [Type index number]'))
            if cho < self.capacity and cho > -1:
                self.deletionfrominventory(cho)
            else:
                print('That location does not exist in your bag.')
                self.destroyitem(-1)
        else:
            index = self.storeAttribute.index(item)
            self.deletionfrominventory(index)
    
    def useinventoryitem(self,player,turncreditsp):

        if len(self.storeAttribute) == 0:
            print("There is nothing in your bag.")
            return player,turncreditsp

        choice = input("Use something? (Enter Valid Index) or Return (r) -> ")
        if choice < str(len(self.storeAttribute)) and choice > "-1":
            choice = int(choice)
            typeofitem = self.storeAttribute[choice].type
            if typeofitem == "Healing Item": #Heals the player
                if player.hp < player.maxhp:
                    if round(player.hp + self.storeAttribute[choice].healing,1) > player.maxhp:
                        player.hp = player.maxhp
                    else:
                        player.hp = round(player.hp + self.storeAttribute[choice].healing,0)
                        print(f"You healed for {round(self.storeAttribute[choice].healing,0)} HP.")
                        turncreditsp -= 1
                        self.destroyitem(self.storeAttribute[choice]) 
                    return player,turncreditsp
                else:
                    print("Your HP is full.")
            
            elif typeofitem == "Story Item": #Makes sure item is not story item
                print("This item cannot be used.")
                return player,turncreditsp

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
        return player,turncreditsp
 
class ItemC:

    itemname = { 
                   1: {'Name':'Shadow Key Fragment','Healing':0,'Type':'Story Item','Attackup':0,'Defenceup':0,'Usable':0},
                   2: {'Name':'Silver Key Fragment','Healing':0,'Type':'Story Item','Attackup':0,'Defenceup':0,'Usable':0},
                   3: {'Name':'Organic Key Fragment','Healing':0,'Type':'Story Item','Attackup':0,'Defenceup':0,'Usable':0},
                   4: {'Name':'Battery','Healing':60,'Type':'Healing Item','Attackup':5,'Defenceup':0,'Usable':1}, 
                   5: {'Name':'Scrap','Healing':80,'Type':'Healing Item','Attackup':0,'Defenceup':2,'Usable':1}, 
                   6: {'Name':'X Attack','Healing':0,'Type':'Supplement Item','Attackup':10,'Defenceup':0,'Usable':1}, 
                   7: {'Name':'X Defence','Healing':0,'Type':'Supplement Item','Attackup':0,'Defenceup':20,'Usable':1}, 
                }

    def __init__(self,Storystate,entype,state):

        if entype == "Enemy":
            item = randint(0,100)
            if item == 99:
                item = randint(6,7)
            else:
                item = randint(4,5)
        elif entype == "Boss" and state != 0:
            item = state
        else:
            item = 5

        self.name = self.itemname[item]['Name']
        self.healing = self.itemname[item]['Healing']*(Storystate/7)
        self.type = self.itemname[item]['Type']
        self.attackup = self.itemname[item]['Attackup']
        self.defenceup = self.itemname[item]['Defenceup']
        self.usable = self.itemname[item]['Usable']

class PlayerC:

    maxhp = 200

    def __init__(self,name,weapon,Storystate) -> None:

        self.name = name
        self.hp = self.recov2fullhp(Storystate)
        self.atk = 10 + weapon.dmg
    
    def recov2fullhp(self,Storystate):
        if Storystate < 3:
            hp = 20
            self.inventorymax = 10
        elif Storystate == 3:
            hp = self.maxhp*.25
            self.inventorymax = 20
        elif Storystate == 4 or Storystate == 5:
            hp = self.maxhp*.5
            self.inventorymax = 30
        elif Storystate == 6 or Storystate == 7:
            hp = self.maxhp
            self.inventorymax = 40
        return hp     

    def playerturn(self,enemy,weapon,Storystate):
 
        if enemy.name == weapon.Attackupval:
            factor = Storystate
        else:
            factor = 0

        enemy.hp = round(enemy.hp - (weapon.dmg + factor),0)
        print(f'You have dealt {weapon.dmg + factor} damage.')
        return enemy
        
    def enemyturn(self,enemy):

        self.hp = round(self.hp-enemy.atk,0)
        print(f'The enemy has dealt {enemy.atk} damage.')
        return self

class EnemyC:
    
    Enemystat = {
                 1: {'name': 'Golem', 'bhp': 75, 'ba': 20, 'Weight': 1, 'Turnfall':1.1, 'Recovery':0.1, 'Healcount':2, 'Fleechance':1},
                 2: {'name': 'Wombie', 'bhp': 30, 'ba': 25, 'Weight': 1,'Turnfall':0.51, 'Recovery':0.2, 'Healcount':3, 'Fleechance':.5 },
                 3: {'name': 'Slime', 'bhp': 18, 'ba': 10, 'Weight': 1,'Turnfall':0.21, 'Recovery':0.1, 'Healcount':10, 'Fleechance':.5 },
                 4: {'name': 'Hellicopeter', 'bhp': 40, 'ba': 30, 'Weight': 2,'Turnfall':1.1, 'Recovery':0.4, 'Healcount':2, 'Fleechance':.1 },
                 }

    def __init__(self,Storystate):

        randomenemy=randint(1,4)
        randomiserha = randint(60,100)
        randomability=randint(1,5)
        if randomability == 5:
            Strongerscaling=1.5
        else:
            Strongerscaling=1
        self.name=self.Enemystat[randomenemy]['name']
        self.maxhp=round(Strongerscaling*self.Enemystat[randomenemy]['bhp']*(randomiserha/100)*(Storystate/7),0)
        self.hp=round(Strongerscaling*self.Enemystat[randomenemy]['bhp']*(randomiserha/100)*(Storystate/7),0)
        self.atk=round(Strongerscaling*self.Enemystat[randomenemy]['ba']*(randomiserha/100)*(Storystate/7),0)
        self.recov=round(self.maxhp*self.Enemystat[randomenemy]['Recovery'],1)
        self.Weight=self.Enemystat[randomenemy]['Weight']
        self.healcount=self.Enemystat[randomenemy]['Healcount'] #Times it can heal a turn
        self.turnfall=self.Enemystat[randomenemy]['Turnfall']
        self.decisionrecall=0
        self.fleechance=self.Enemystat[randomenemy]['Fleechance']
        self.keyID=0
        self.identifier="Enemy"

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
                    if self.healcount > 0:
                        return 'heal'
                    else:
                        return 'attack'
                else:
                    return 'attack'
            elif recklessness == 1: # Not Reckless
                if self.hp < weapon.dmg:
                    if self.healcount > 0:
                        return 'heal'
                    else:
                        return 'attack'
                else:
                    return 'attack'
        else:
            return 'attack'
        print("IDK Bro")
                    
    def Postbattle(self,Player,pos,Storystate):
        #DO NOT REMOVE PLAYER FROM ARGUMENTS, WILL BREAK FUNCTION
        return pos,Storystate

class BossC(EnemyC):
    
    Bossstat = { 1: {'name': 'The Undead Golaith', 'bhp': 50.0, 'ba': 10.0, 'Weight': 1, 'Turnfall':1.1, 'Recovery':0.1,'Phase':2, 'Healcount':5, 'Fleechance':1, 'KeyID':1},
                 2: {'name': 'The Forest Guardian', 'bhp': 30.0, 'ba': 15.0, 'Weight': 1,'Turnfall':1.1, 'Recovery':0.4,'Phase':3, 'Healcount':5, 'Fleechance':.5, 'KeyID':2},
                 3: {'name': 'The Grand Slime', 'bhp': 100.0, 'ba': 10.0, 'Weight': 1,'Turnfall':0.51, 'Recovery':0.5,'Phase':2, 'Healcount':5, 'Fleechance':.5, 'KeyID':3},
                 4: {'name': 'The Stargazer', 'bhp': 100.0, 'ba': 30.0, 'Weight': 2,'Turnfall':1.1, 'Recovery':0.1,'Phase':4, 'Healcount':2, 'Fleechance':.1, 'KeyID':1},
                 }
    
    BossstatPhMid = { 
                 2: {'name': 'The Forest Guardian', 'bhp': 30.0, 'ba': 5.0, 'Weight': 0,'Turnfall':1.1, 'Recovery':0.4,'Fleechance':.5 },
                 3: {'name': 'The Grand Slime', 'bhp': 100.0, 'ba': 5.0, 'Weight': 1,'Turnfall':0.51, 'Recovery':0.5,'Fleechance':.5 },
                 4: {'name': 'The Stargazer', 'bhp': 100.0, 'ba': 3.0, 'Weight': 2,'Turnfall':1.1, 'Recovery':0.1,'Fleechance':.1 },
                 }

    BossstatPhFin = { 
                 1: {'name': 'The Undead Golaith', 'bhp': 30.0, 'ba': 6.5, 'Weight': 1, 'Turnfall':0.51, 'Recovery':0.2,'Fleechance':1},
                 2: {'name': 'The Forest Guardian', 'bhp': 40.0, 'ba': 20.0, 'Weight': 0,'Turnfall':1.1, 'Recovery':0.4,'Fleechance':.5 },
                 3: {'name': 'The Grand Slime', 'bhp': 100.0, 'ba': 10.0, 'Weight': 1,'Turnfall':0.51, 'Recovery':0.5,'Fleechance':.5 },
                 4: {'name': 'The Stargazer', 'bhp': 100.0, 'ba': 30.0, 'Weight': 2,'Turnfall':1.1, 'Recovery':0.1,'Fleechance':.1 },
                 }

    def __init__(self,Storystate,boss):

        super().__init__(Storystate)
        self.index = boss
        self.name=self.Bossstat[self.index]['name']
        self.maxhp=round(self.Bossstat[self.index]['bhp'],0)
        self.hp=round(self.Bossstat[self.index]['bhp'],0)
        self.atk=round(self.Bossstat[self.index]['ba'],0)
        self.recov=self.Bossstat[self.index]['bhp']*self.Bossstat[self.index]['Recovery']
        self.Weight=self.Bossstat[self.index]['Weight']
        self.healcount=self.Bossstat[self.index]['Healcount'] #Times it can heal a turn
        self.turnfall=self.Bossstat[self.index]['Turnfall']
        self.phase=self.Bossstat[self.index]['Phase']
        self.keyID=self.Bossstat[self.index]['KeyID']
        self.identifier="Boss"

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
        
    def atkread(self):
        strcount=self.name+str(self.phase)
        linecounter=0
        savestatecount=0
        file = open('EnemyData.txt', 'r') # Calls the file we are specifying

        for lines in file: 
            editlines=lines.strip("\n") # We want to get rid of \n to clean up the output, no spaces between lines.
            numend="End"+strcount # End1, End2 in txt file
            if editlines == numend:
                savestatecount=0
            elif savestatecount == 1:
                if self.hp == self.maxhp:
                    time.sleep(0.1)
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

    def FinalPhase(self):
        self.name=self.BossstatPhFin[self.index]['name']
        self.maxhp=round(self.BossstatPhFin[self.index]['bhp'],0)
        self.hp=round(self.BossstatPhFin[self.index]['bhp'],0)
        self.atk=round(self.BossstatPhFin[self.index]['ba'],0)
        self.recov=self.BossstatPhFin[self.index]['bhp']*self.BossstatPhFin[self.index]['Recovery']
        self.Weight=self.BossstatPhFin[self.index]['Weight']
        self.turnfall=self.BossstatPhFin[self.index]['Turnfall']

    def MidPhase(self):
        self.name=self.BossstatPhMid[self.index]['name']
        self.maxhp=round(self.BossstatPhMid[self.index]['bhp'],0)
        self.hp=round(self.BossstatPhMid[self.index]['bhp'],0)
        self.atk=round(self.BossstatPhMid[self.index]['ba'],0)
        self.recov=self.BossstatPhMid[self.index]['bhp']*self.BossstatPhMid[self.index]['Recovery']
        self.Weight=self.BossstatPhMid[self.index]['Weight']
        self.turnfall=self.BossstatPhMid[self.index]['Turnfall']

    def Postbattle(self,Player,pos,Storystate):
        if self.phase == 3:
            if self.hp < 1:
                self.phase -= 1
                self.hp = self.maxhp
                self.MidPhase()
        if self.phase == 2:
            if self.hp < 1:
                self.phase -= 1
                self.hp = self.maxhp
                self.FinalPhase()
        elif self.phase == 1:
            if self.hp < 1:
                Storystate += 1
                return pos,Storystate
            
        if Player.hp < 1:
            if Storystate == 3:
                pos = [2,22]
            elif Storystate == 4:
                pos = [5,19]

        return pos,Storystate

# Weapon,Player,Enemy,Storystate,flee,Inventory 

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
    elif Class.__class__.__name__ == 'EnemyC' or Class.__class__.__name__ == 'BossC':
        strcount='Check'
    elif Class.__class__.__name__ == 'InventoryC':
        strcount='Inventory'
    elif Class.__class__.__name__ == 'ItemC':
        strcount='Item'
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
            if Class.store != []:
                time.sleep(0.1)
                linecounter+=1
                if linecounter == 3:
                    print('     Access ID ')
                    for i in Class.index:
                        print(f'         {i}      {Class.quantity[i]}  {Class.store[i]}')
                else:
                    pass
                print(editlines)
            else:
                pass

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

# Randomises the enemy/boss
def battle(Storystate,name,Inventory,Weapon,pos,Enemy):

    Player,Enemy = battleready(Storystate,name,Weapon,pos)
    time.sleep(1)
    clear()
    Player,Enemy,flee,pos,Storystate = turn(Weapon,Player,Enemy,Storystate,Inventory,pos)
    Inventory,Weapon = result(Weapon,Player,Enemy,flee,Inventory,Storystate)
    return Player,Weapon,Inventory,pos,Storystate

def battleready(Storystate,name,Weapon,pos):
    
    Player = PlayerC(name,Weapon,Storystate)
    if pos == [2,21] and Storystate == 3:
        Enemy = BossC(Storystate,1)
        bossanimation(Storystate)
    elif pos == [5,20] and Storystate == 4:
        Enemy = BossC(Storystate,2)
        bossanimation(Storystate)
    elif pos == [3,3] and Storystate == 6:
        Enemy = BossC(Storystate,3)
        bossanimation(Storystate)
    else:
        Enemy = EnemyC(Storystate)
        print (f"You encounter a {Enemy.name}!")

    return Player,Enemy

def bossanimation(Storystate):

    pattern = ["Glow",Storystate,"Glow",Storystate,"Glow","Glow1","Glow2","Glow3","Glow4","Glow5","Glow6","Glow7"]
    for i in pattern:
        clear()
        file = open('Map.txt', 'r',encoding = 'utf8')
        strcount=str(i) # Converts count into string, cause the numbers are str in .txt file
        savestatecount=0
        for lines in file: 
            editlines = lines.strip() # We want to get rid of \n to clean up the output, no spaces between lines.
            numend="End"+strcount # End1, End2 in txt file

            if editlines == numend: 
                savestatecount=0

            if savestatecount == 1:
                print(editlines)
            else:
                pass
            
            if editlines == strcount: 
                savestatecount=1
        file.close()
        time.sleep(0.2)

# Gets the result of the battle
def result(Weapon,Player,Enemy,flee,Inventory,Storystate):
    if flee == 1:
        print('You got away successfully.')
    elif Player.hp > 1 and Enemy.hp < 1:
        Item1 = ItemC(Storystate,Enemy.identifier,Enemy.keyID)
        Item2 = ItemC(Storystate,Enemy.identifier,0)
        print('Player wins')
        print(f'You obtained 1x {Item1.name}!')
        Inventory.additem(Item1)
        print(f'You obtained 1x {Item2.name}!')
        Inventory.additem(Item2)
        Weapon=weaponroll(Weapon,Storystate)
    elif Player.hp < 1 and Enemy.hp > 1:
        print('Enemy wins')
    elif Player.hp < 1 and Enemy.hp < 1:
        print('No one won.')
    else:
        print('Debug Error')
    input('Press enter to continue')

    return Inventory,Weapon
    
# Rolls a new weapon
def weaponroll(currentweapon,Storystate):
    dm = 0 # Decision made
    Weaponnew=WeaponC(Storystate)
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

# Turn based Combat Begins here
def turn(Weapon,Player,Enemy,Storystate,Inventory,pos):
    flee = 0
    while Player.hp >= 1 and Enemy.hp >= 1 and flee == 0:
        Enemy.decisionrecall=0

        clear()
        Enemy.atkread()
        print(f'     Your hp: {Player.hp} | Enemy hp: {Enemy.hp}')
        Player,Enemy,flee = checkWeight(Weapon,Player,Enemy,Storystate,flee,Inventory)
        pos,Storystate = Enemy.Postbattle(Player,pos,Storystate)
        input('Press enter to continue')

        if flee == 1:
            break
    return Player,Enemy,flee,pos,Storystate

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

# Player Decision
def fightplayer(Weapon,Player,Enemy,Storystate,flee,Inventory):
    turncreditsp=1
    while turncreditsp > 0:
        print('|--------------------------------------|')
        choice = input(' |X|Attack  |Y|Check  |Z|Inv  |O|Run  ->')
        if choice == 'X':
            turncreditsp -= Weapon.atk_frequency
            Enemy = Player.playerturn(Enemy, Weapon, Storystate)
        elif choice == 'Y':
            UIread(Enemy)
        elif choice == 'Z':
            UIread(Inventory)
            Player,turncreditsp=Inventory.useinventoryitem(Player,turncreditsp)
        elif choice == 'O':
            if Enemy.__class__.__name__ == 'EnemyC':
                if random() < Enemy.fleechance:
                    turncreditsp -= 1
                    flee = 1
                else:
                    print('You failed to escape')
                    turncreditsp -= 1
                    pass
            else:
                print("You cannot escape from a boss fight")

    return Enemy,flee

def fightenemy(Weapon,Player,Enemy):
    print('|--------------------------------------|')
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

## Past this point is the main map controls ##

def map(countmap,pos):
    if pos == [5,36]:
        sleep = 0.1
    else:
        sleep = 0
    file = open('Map.txt', 'r',encoding = 'utf8')
    strcount=str(countmap) # Converts count into string, cause the numbers are str in .txt file
    savestatecount=0
    internalcounter = -1 # Counts the lines of the text file we are generating, follows list notation, 0,1,2,3 we will add one later.
    for lines in file: 
        editlines = lines.strip() # We want to get rid of \n to clean up the output, no spaces between lines.
        numend="End"+strcount # End1, End2 in txt file

        if editlines == numend: 
            savestatecount=0

        if savestatecount == 1:
            internalcounter+=1
            time.sleep(sleep)
            if internalcounter == pos[0]: 
                editlines = str(editlines[:pos[1]])+"X"+str(editlines[pos[1]+1:])
                print(editlines)
            elif editlines == numend:
                savestatecount=0
            else: 
                print(editlines)
        else:
            pass
        
        if editlines == strcount: 
            savestatecount=1
    
    file.close()
    return countmap,pos

def movement(countmap,pos):
    
    strcount=str(countmap) # Converts count into string, cause the numbers are str in .txt file
    savestatecount = 0
    internalcounter = -1 # Counts the lines of the text file we are generating, follows list notation, 0,1,2,3 we will add one later.
    
    map(countmap,pos)
    move=str(input("Which direction do you want to move in? [n] [s] [e] [w] [use]"))

    checklist=["n","s","e","w","use"]
    for i in checklist: # Check if input is valid
        if i == move:
            clear=1    

    file = open('Map.txt', 'r',encoding = 'utf8')

    for lines in file:
        editlines = lines.strip()
        numend="End"+strcount # End1, End2 in txt file        

        if savestatecount == 1:
            internalcounter+=1
            #Movement commands, checks all bits adjacent to the current position.
            if internalcounter == pos[0]-1  and move == "n": 
                if editlines[pos[1]] == "." or editlines[pos[1]+1] == "L" or editlines[pos[1]+1] == "!":
                    pos[0] -= 1  #North
                else:
                    print("You can't move north.")
                    time.sleep(1)
            elif internalcounter == pos[0] and move == "w":
                if editlines[pos[1]-1] == "." or editlines[pos[1]-1] == "@" or editlines[pos[1]+1] == "!" or editlines[pos[1]+1] == "*":
                    pos[1] -= 1  #West
                else:
                    print("You can't move west.")
                    time.sleep(1)
            elif internalcounter == pos[0]and move == "e":
                if editlines[pos[1]+1] == "." or editlines[pos[1]+1] == "@" or editlines[pos[1]+1] == "*":
                    pos[1] += 1  #East
                else:
                    print("You can't move east.")
                    time.sleep(1)
            elif internalcounter == pos[0]+1 and move == "s":
                if editlines[pos[1]] == ".":
                    pos[0] += 1  #South
                    break
                else:
                    print("You can't move south.")
                    time.sleep(1)
            elif editlines == numend: 
                savestatecount=0
            else: 
                pass
        
        if editlines == strcount: 
            savestatecount=1
            
    file.close()
    return pos

def story_progressfier(Storystate,pos):
    if Storystate == 1 and pos == [4,36]:
        Storystate = 2
    elif Storystate == 2 and pos == [4,29]:
        Storystate = 3
    return Storystate

## This declares the Main Variables of our program ##

def Var_declaration():
    #Placed key variables in a function to allow the whole game to reset as well as saving.
    Storystate=4
    #[5,17]
    pos=[5,36]

    return Storystate, pos

## Pass this point is the main function ##

def main():
    Storystate,pos = Var_declaration()

    name = input('What is your name?')
    Weapon = WeaponC(Storystate)
    Player = PlayerC(name,Weapon,Storystate)
    Inventory = InventoryC(Player)
    while True:
        clear()
        pos = movement(Storystate,pos)
        Storystate = story_progressfier(Storystate,pos)
        Enemyencounter = randint (1,3) # Randomises for enemies everytime you move.
        if Enemyencounter == 2 or pos == [2,21] or pos == [5,20]: # Change it back to normal modifiers
            Player, Weapon, Inventory, pos, Storystate = battle(Storystate,name,Inventory,Weapon,pos,0)
            clear()
        else:
            pass

main()