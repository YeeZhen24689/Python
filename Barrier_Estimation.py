#--------------------------------------------------------------------------#
#                         Curve estimator example                          #
#--------------------------------------------------------------------------#

import matplotlib.pyplot as plt
import numpy as np

#PRINT MY TEST TRACKS FOR TROUBLESHOOTING#
with np.load('slam_test_tracks.npz') as data:
    a=data['track1_1']
    b=data['track1_2']
    c=data['track1_3']
print(c)

def quadratic_coefficient_generator(x,y): #Computes a quadratic function from three points#
    #INPUT# Takes in an array of three most recent x and y values.
    
    #Code Block Exp# Solves the quadratic equation as Ax = b where A is our quadratic function matrix
    #Code Block Exp# x = our 3 by 1 array of coefficients a, b and c
    A = np.array([[x[0]**2,x[0],1],[x[1]**2,x[1],1],[x[2]**2,x[2],1]])
    try:
        Ainverse = np.linalg.inv(A)
    except np.linalg.LinAlgError:
        coefficients=np.array([[0],[0],[0]])
        return coefficients
    b = np.array([[y[0]],[y[1]],[y[2]]])
    coefficients = Ainverse@b
    
    return coefficients

def perpendicular_derivative(coefficient,x,y): #Computes the gradient and y-int of the perpendicular line from a set of given points
    a = coefficient[0]
    b = coefficient[1]
    c = coefficient[2]

    if a == 0: #If this line is a linear line
        perpendicular_derivative_coef = np.array([1,1,1])*-1/b #Just invert the coefficient b
        c = np.array([1,1,1])*(y - x/(perpendicular_derivative_coef))
    elif a < 0.01 and b < 0.01:
        perpendicular_derivative_coef = np.array([1,1,1])*y[2]
        c = np.array([1,1,1])*(y[2]-3)
    else: #If this line is a higher order line (2nd)
        perpendicular_derivative_coef = -1/(2*a*x+b)
        c = y - x*(perpendicular_derivative_coef)

    return perpendicular_derivative_coef,c

def distance(x,y,gradient_of_perpendicular,a):
    track_width = 3
    if a < 0:
        isslopedown = 1
    else:
        isslopedown = -1
    
    new_x = (isslopedown*np.sqrt(track_width**2/(1+gradient_of_perpendicular**2))+x)
    new_y = (isslopedown*(-new_x+x)*gradient_of_perpendicular+y)

    return new_x,new_y

# MOST IMPORTANT BLOCK OF CODE#
def pointgenerator(current_x,current_y,x_estimate,y_estimate):
    dee_x = (current_x[1]-current_x[0])
    dee_y = (current_y[1]-current_y[0])
    if dee_x == 0:
        gradweight = 1
    else:
        gradweight = 1.16*2/(1 + np.exp(abs(dee_y/dee_x))) #golden ratio apparently

    new_x = x_estimate[len(x_estimate)-1]+dee_x*gradweight
    new_y = y_estimate[len(y_estimate)-1]+dee_y*gradweight

    #MAINLY FOR TROUBLESHOOTING#
    dist = np.sqrt(np.square(new_x-current_x[1])+np.square(new_y-current_y[1]))
    if dist != 3:
        error = 3 - dist
        print(error)

    print(f"My distance is: {dist}.")
    
    return new_x,new_y

x,y = np.array([3.,6.,9.]),np.array([1.5,1.5,1.5])
current_x,current_y = x[len(x)-3:],y[len(x)-3:]

#Coefficient declaration#
coefficients = quadratic_coefficient_generator(current_x,current_y)
gradient, c = perpendicular_derivative(coefficients,current_x,current_y)
new_x,new_y = distance(current_x,current_y,gradient,coefficients[0])

#Estimation Declaration#
x_estimate,y_estimate = np.array([]),np.array([])
x_estimate,y_estimate = np.append(x_estimate,new_x[0:1]),np.append(y_estimate,new_y[0:1])

#Visualiser#
test_x = np.linspace(x[len(x)-3],x[len(x)-1],100)
test_y = coefficients[0]*(test_x**2)+coefficients[1]*test_x+coefficients[2]
test_x2 = np.linspace(x[len(x)-3],x[len(x)-1],100)
test_y2 = gradient[0]*test_x2 + c[1]
test_x3 = np.linspace(x[len(x)-3],x[len(x)-1],100)
test_y3 = -1/gradient[0]*test_x3 + (current_y[1] - current_x[1]*(-1/gradient[1]))
#End Visualiser#

plt.ion
fig = plt.figure()
axis = fig.add_subplot(111)
line1 = axis.plot(x,y,'r')[0]
line2 = axis.plot(x_estimate,y_estimate,'b')[0]
line3 = axis.plot(test_x,test_y,'g')[0]
line4 = axis.plot(test_x2,test_y2,'orange')[0]
line5 = axis.plot(test_x3,test_y3,'purple')[0]
point3 = axis.plot(x,y,'ro')[0]
point4 = axis.plot(current_x[1],current_y[1],'bo')[0]
plt.show(block=False)

xcorrd = [12,15,17.5,19.5,20.5,21,21,20.5,19.5,17.5,17,16]
ycorrd = [1.5,1.5,1,0,-1.5,-3,-4,-5.5,-7,-8,-8.5,-9.5]

#xcorrd = np.linspace(0,7,100)
#ycorrd = -0.4*np.power(xcorrd,3)+1.9*np.power(xcorrd,2)+2.4*xcorrd

for i in range(0,len(xcorrd)):
    plt.xlim([0, 25]) 
    plt.ylim([-20, 5])
    x = np.append(x,float(xcorrd[i]))
    y = np.append(y,float(ycorrd[i]))

    current_x,current_y = x[len(x)-2:],y[len(x)-2:]
    new_x,new_y = pointgenerator(current_x,current_y,x_estimate,y_estimate)
    x_estimate,y_estimate = np.append(x_estimate,new_x),np.append(y_estimate,new_y)

    line1.remove()
    line2.remove()
    point3.remove()
    point4.remove()

    line1 = axis.plot(x,y,'r')[0]
    line2 = axis.plot(x_estimate,y_estimate,'b')[0]
    point3 = axis.plot(new_x,new_y,'bo')[0]
    point4 = axis.plot(current_x[1],current_y[1],'ro')[0]

    plt.show(block=False)
    plc = input("next")






