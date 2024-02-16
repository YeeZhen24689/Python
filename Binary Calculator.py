
def adding(binarynum1,binarynum2):
    result = []
    bn1 = []
    bn2 = []
    for i in binarynum1:
        bn1.append(int(i))
    for i in binarynum2:
        bn2.append(int(i))
    flipbn1 = bn1.reverse()
    flipbn2 = bn2.reverse()
    carry = 0
    switch = 'off'
    for i in range(len(bn1)):

        output = bn1[i] + bn2[i] + carry
        if output == 3:
            output = 1
            carry = 1
        elif output == 2:
            output = 0
            carry = 1
        else:
            carry = 0

        result.append(str(output))
        if i == len(bn1)-1:
            if output == 2:
                switch = 'on'
                result.append(str(1))
                
        print(result)
    result.reverse() 
    result = "".join(result) 
    print(result)

def twoscomplement(binarynum):
    newappend = []
    for i in binarynum:
        if i == '1':
            newappend.append('0')
        else:
            newappend.append('1')
    newappend=''.join(newappend)


def main():
    num1 = input("Enter your first binary number -> ")
    num2 = input("Enter your second binary number -> ")
    adding(num1,num2)
    twoscomplement(num1)

main()

