import turtle

def my_turtle():
    turtle.color("red")
    turtle.begin_fill()
    turtle.forward(200)
    turtle.left(128)
    turtle.forward(200)
    turtle.left(128)
    turtle.home()
    turtle.setheading(110)
    turtle.end_fill()
    
    
    
def turtle_state():
    var1=turtle.isdown()
    var2=turtle.heading()
    varx=turtle.xcor()
    vary=turtle.ycor()
    var3=turtle.shapesize()
    print("turtle is down?",var1)
    print("current angle: ",var2)
    print("Xcor :",varx,"ycor: ",vary)
    print("this is the size: ",var3)

def square(mysize):
    turtle.forward(mysize)
    turtle.left(90)
    turtle.forward(mysize)
    turtle.left(90)
    turtle.forward(mysize)
    turtle.left(90)
    turtle.forward(mysize)
    turtle.left(90)
    
   
    
def main():
    size=input("Enter size of square: ")
    square(int(size))
    my_turtle()
    #turtle_state()
    input("press any key to contiune:")

main()
