from tkinter import ARC
import turtle
def draw_circle(x,y,myradius,fillcolor):
    turtle.up()
    turtle.goto(x,y)
    turtle.pencolor("black")
    turtle.fillcolor(fillcolor)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(myradius)
    turtle.end_fill()

def centered_circle(x,y,myradius,fillcolor):
    turtle.up()
    turtle.goto(x,y)
    turtle.forward(myradius)
    turtle.left(90)
    turtle.fillcolor(fillcolor)
    turtle.pencolor("black")
    turtle.down()
    turtle.begin_fill()
    turtle.circle(myradius)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(myradius)
    turtle.left(180)


def draw_smily(x,y,myradius,fillcolor):
    centered_circle(x,y,myradius,"yellow")
    tenth=myradius/10
    centered_circle(x,y,tenth,"pink")
    quarter=myradius/4

    draw_eye(x+quarter+tenth,y+quarter,quarter,fillcolor)
    draw_eye(x-quarter-tenth,y+quarter,quarter,fillcolor)

def tweak(speed,tracer):
    turtle.speed(speed)
    turtle.tracer(tracer)
  
def draw_eye(x,y,radius,eyecolor):
    centered_circle(x,y,radius,"white")
    centered_circle(x,y,radius/2,eyecolor)
    centered_circle(x,y,radius/4,"black")
    


def main():
    #draw_circle(20,30,50,"Blue")
    #draw_circle(0,-150,90,"red")
    #draw_circle(-200,0,100,"green")
    tweak(0,False)
    draw_smily(100,100,90,"green")
    input("stp")

main()