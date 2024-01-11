import math
import time
print("|------------------------|")
print("|-The Quadratic Equation-|")
print("|--------Solve [1]-------|")
print("|---Facotrize---|")
print("|------------------------|")
choice = input("Make your choice -->")
while True:
    if choice == "x":
        try:
            while True:
                UI = [int(num)for num in input("Please enter your a, b and c value with a space after each.").split()]
                if len(UI) != 3:
                    print("You are not entering the right amount of values.")
                    True
                else:
                    break    
            a = UI[0]
            b = UI[1]
            c = UI[2]
            print(f"UI:{UI},a:{a},b:{b},c:{c}")
            quad1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
            quad2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
            print(f"Your two values are:{quad1},{quad2}")
            break
        except ValueError:
            time.sleep(1)
            print("Please only enter integers.")
    elif choice == "y":    
        try:
            while True:
                UI = [int(num)for num in input("Please enter your a, b and c value with a space after each.").split()]
                if len(UI) != 3:
                    print("You are not entering the right amount of values.")
                else:
                    break    
            a = UI[0]
            b = UI[1]
            c = UI[2]
            for i in range(a):
                i += 1
                print(i)
                a1 = a/i
                if a%a1 == 0:
                    for x in range(c):
                        print("2")
                        x += 1
                        c1 = c/x
                        if c%c1 == 0:
                            print("3")
                            try1=(a1*c1)+(i*x)
                            try2=(a1*x)+(i*c1)
                            print(try1,try2,a1*c1,i*x)
                            if try1==b:
                                print(f"The factorized expression is ({int(a1)}x+{x})({i}x+{int(c1)}).")
                            elif try2==b:
                                print(f"The factorized expression is ({int(a1)}x+{x})({i}x+{int(c1)}).")
                            else:
                                break
                            break
                        break
                    break
                break
            break
                        
        except ValueError:
            time.sleep(1)
            print("Please only enter integers.")
    else:
         print("Please enter either x or y. (Case Sensitive)")
         break
