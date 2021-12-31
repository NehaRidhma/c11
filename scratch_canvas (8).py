import turtle
d={'shape':'square','size':100,'angle':90,'color':'purple'}

for i in range(4):
    turtle.pencolor(d['color'])
    turtle.shape(d['shape'])
    turtle.forward(d['size'])
    turtle.left(d['angle'])
                     

   