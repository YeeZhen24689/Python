def bin2dec():
    answerval = 0
    x = str(input("Please enter your binary value"))
    lenx = len(x)
    for i in x:
        iteration = lenx - 1
        if i == "1":
            answerval += 2**iteration
        else:
            pass
        if lenx ==0:
            break
        else:
            lenx -= 1
        iteration += 1
    print(answerval)

def hex2dec():
    answerval = 0
    iterate = 0
    hexdict = {
        "A" : 10,
        "B" : 11,
        "C" : 12,
        "D" : 13,
        "E" : 14,
        "F" : 15
    }
    x = str(input("Please enter your hexadecimal value."))
    lenx = len(x)-1
    for i in x:
        try:
            number = int(i)
        except ValueError:
            number = hexdict[i]
        answerval += number * 16**(lenx-iterate)
        iterate += 1
    print (answerval)


def dec2bin():
    while True:
        binconversion=[]
        x=int(input("Enter your denary number here."))
        xnew=x
        while x != 0:
            x=int(x)/2
            if (x).is_integer() == False:
                x=x-0.5
                binconversion=["1"]+binconversion
            elif (x).is_integer() == True:
                binconversion=["0"]+binconversion
        print(f"Your original denary number is {xnew}, its binary equivalent is {''.join(binconversion)}.")

def main():
    x = input("Which converter are your looking for? [d2b] [b2d] [h2b]")
    if x == 'd2b':
        dec2bin()
    elif x ==  'b2d':
        bin2dec()
    elif x == 'h2b':
        hex2dec()
    else:
        print("Not Valid")

main()