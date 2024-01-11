import time
import os

clear = lambda : os.system('cls')

#6 Parts to the story, story state defines the part of the story you are in
storystate=1
pos=[5,36]
#file = open('Map.txt', encoding = 'utf8') # Encode UTF-8 to allow for special characters.

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
                if editlines[pos[1]] == ".":
                    pos[0] -= 1  #North
                else:
                    print("You can't move north.")
                    time.sleep(1)
            elif internalcounter == pos[0]and move == "w":
                if editlines[pos[1]-1] == ".":
                    pos[1] -= 1  #West
                else:
                    print("You can't move west.")
                    time.sleep(1)
            elif internalcounter == pos[0]and move == "e":
                if editlines[pos[1]+1] == ".":
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
    return countmap,pos

def story_progressfier(storystate,pos):
    if storystate == 1 and pos == [4,36]:
        storystate = 2
    elif storystate == 2 and pos == [4,29]:
        storystate = 3
    elif storystate == 3 and pos == [5,1000]: #TBC
        storystate = 4
    elif storystate == 4 and pos == [5,29000]: #TBC
        storystate = 5
    elif storystate == 5 and pos == [5,29000]: #TBC
        storystate = 6
    elif storystate == 6 and pos == [5,29000]: #TBC
        storystate = 7
    return storystate

clear()
while True: 
    cmp,pos = movement(storystate,pos)
    storystate = story_progressfier(storystate,pos)
    clear()
