def mapp():print('map!');return 

def stats():print('stat!');return

def inve():print('inventory!');return

import time

count=1

def storyread(count):
    strcount=str(count) # Converts count into string, cause the numbers are str in .txt file
    savestatecount=0
    file = open('Storylin.txt', 'r') # Calls the file we are specifying
    loop = 0

    for lines in file: 
        editlines=lines.replace("\n","") # We want to get rid of \n to clean up the output, no spaces between lines.
        numend="End"+strcount # End1, End2 in txt file
        
        if savestatecount == 1:
            loop+=1
            time.sleep(1)
            if editlines == "Inv":    inve()
            elif editlines == "Map":  mapp()
            elif editlines == "Stat": stats()
            elif editlines == numend: savestatecount=0
            else: print(editlines + str(loop))
        else:
            pass
        
        if editlines == strcount: 
            savestatecount=1
            
    file.close()
    count += 1
    return count

count = storyread(count)
count = storyread(count)





