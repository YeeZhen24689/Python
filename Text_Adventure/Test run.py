score=0
retrys=5
lives=5
print("Welcome")
name=input("please enter name")
form=input("please enter form")
while lives > 0:
   Q1=input("1)What is 4*4?")
   if Q1=="16":
        print("Correct")
        score = score + 1
        print(score)
   else:
        print("Wrong")
        retrys = retrys - 1
        print("Lives Left:")
        print(retrys)
        
   t=input("2)What is 56+44?")
   if t=="100":
        print("Correct")
        score = score + 1
        print(score)
   else:
        print("Wrong")
        retrys = retrys - 1
        print("Lives Left:")
        print(retrys)

   h=input("3)What is 26*490?")
   if h=="12740":
        print("Correct")
        score = score + 1
        print(score)
   else:
        print("Wrong")
        retrys = retrys - 1
        print("Lives Left:")
        print(retrys)

   a=input("4)What is 30/4+456?")
   if a=="463.5":
        print("Correct")
        score = score + 1
        print(score)
   else:
        print("Wrong")
        retrys = retrys - 1
        print("Lives Left:")
        print(retrys)

   g=input("5)What is 26*4-567?")
   if g=="-463":
        print("Correct")
        score = score + 1
        print(score)
   else:
        print("Wrong")
        retrys = retrys - 1
        print("Lives Left:")
        print(retrys)
        
   l=input("6)What is 1*0?")
   if l=="0":
        print("Correct")
        score = score + 1
        print(score)
   else:
        print("Wrong")
        retrys = retrys - 1
        print("Lives Left:")
        print(retrys)

   u=input("7)What is 495687-6875*56864?")
   if u=="390444313":
        print("Correct")
        score = score + 1
        print(score)
   else:
        print("Wrong")
        retrys = retrys - 1
        print("Lives Left:")
        print(retrys)

   a=input("8)What is 89/4+7?")
   if a=="29.25":
        print("Correct")
        score = score + 1
        print(score)
   else:
        print("Wrong")
        retrys = retrys - 1
        print("Lives Left:")
        print(retrys)
   print(name)
   print(form)
   score=score/8*100
   print("Score")
   print(score)
   print("This is out of 100")
   print("Retries")
   print(retrys)
