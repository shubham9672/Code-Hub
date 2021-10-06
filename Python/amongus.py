import turtle

class body:
    def __init__(self,color,t) -> None:
        self.color=color
        self.t=t

    def ga(self):
        self.t.pensize(10)
        self.t.fillcolor(self.color)
        self.t.begin_fill()

        self.t.right(90)
        self.t.forward(50)
        self.t.right(180)
        self.t.circle(40,-180)
        self.t.right(180)
        self.t.forward(200)

        self.t.right(180)
        self.t.circle(100,-180)

        self.t.backward(20)
        self.t.left(15)
        self.t.circle(500,-20)
        self.t.backward(20)

        self.t.circle(40,-180)
        self.t.left(7)
        self.t.backward(50)

        self.t.up()

        self.t.left(90)
        self.t.forward(10)
        self.t.right(90)
        self.t.down()

        self.t.right(240)
        self.t.circle(50,-70)

        self.t.end_fill()
        self.t.up()
        pass


    

    def cokh(self):
        self.t.up()

        self.t.right(230)
        self.t.forward(100)
        self.t.left(90)
        self.t.forward(20)
        self.t.right(90)

        self.t.down()
        self.t.fillcolor('white')
        self.t.begin_fill()

        self.t.right(150)
        self.t.circle(90, -55)

        self.t.right(180)
        self.t.forward(1)
        self.t.right(180)
        self.t.circle(10, -65)
        self.t.right(180)
        self.t.forward(110)
        self.t.right(180)
        
        self.t.circle(50, -190)
        self.t.right(170)
        self.t.forward(80)

        self.t.right(180)
        self.t.circle(45, -30)

        self.t.end_fill()
        self.t.up()
        pass

    def bag(self):
        self.t.up()
        self.t.right(60)
        self.t.forward(100)
        self.t.right(90)
        self.t.forward(75)

        self.t.fillcolor(self.color)
        self.t.begin_fill()

        self.t.down()
        self.t.forward(30)
        self.t.right(255)

        self.t.circle(300, -30)
        self.t.right(260)
        self.t.forward(36)

        self.t.end_fill()
        self.t.up()
        
        # self.t.goto(14,250)
        # self.t.pensize(1)
        # self.t.down()

        # self.t.fillcolor('green')
        # self.t.begin_fill()
        # self.t.right(-90)
        # self.t.forward(30)
        # self.t.left(15)
        # self.t.forward(10)
        # self.t.right(120)
        # self.t.forward(20)
        # self.t.right(90)
        # self.t.forward(30)

        # self.t.end_fill()
        # self.t.hideturtle()


        
if __name__ =="__main__":
    j=turtle.Turtle()

    obj=body('red',j)
    obj.ga()
    obj.cokh()
    obj.bag()
    
    caption=turtle.Turtle()
    caption.color('red')
    caption.penup()
    caption.goto(0,-250)
    caption.write("Among Us",align="center" ,font=("Helvatica",20,"normal"))
    caption.hideturtle()
    turtle.done()