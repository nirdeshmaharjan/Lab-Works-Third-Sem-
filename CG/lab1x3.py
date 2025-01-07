import math 
x1=int(input("enter the number"))
y1=int(input("enter the number"))
theta=int(input("angle"))
theta1=math.radians(theta)
x2=x1*math.cos(theta1)-y1*math.sin(theta1)
y2=x1*math.sin(theta1)+y1*math.cos(theta1)
print("rotated coordinates",x2,y2)