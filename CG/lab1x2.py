
x1=int(input("enter the number"))
y1=int(input("enter the number"))
x2=int(input("enter the second number"))
y2=int(input("enter the second number"))
def distance(x1,x2,y1,y2):
    distance=((x2-x1)**2 + (y2-y1)**2)**0.5
    print(distance)

distance(x1,x2,y1,y2)

