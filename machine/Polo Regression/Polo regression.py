#we have registered 18 cars as they were passing a certain tollbooth.
#We have registered the car's speed, and the time of day (hour) the passing occurred
#The x-axis represents the hours of the day and the y-axis represents the speed

#Import numpy and matplotlib then draw the line of Polynomial Regression
import numpy
import matplotlib.pyplot as plt

#Create the arrays that represent the values of the x and y axis
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

#NumPy has a method that lets us make a polynomial model
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

#Then specify how the line will display, 
# we start at position 1, and end at position 22
myline = numpy.linspace(1, 22, 100)
#Predict the speed of a car passing at 17:00
speed = mymodel(17)

#Draw the original scatter plot
plt.scatter(x, y)
#Draw the line of polynomial regression
plt.plot(myline, mymodel(myline))
#Display the diagram
plt.show()
print(speed)