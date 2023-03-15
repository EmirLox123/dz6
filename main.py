import turtle


#тут что бы создать экземпляр надо было сделать turtle.Pen() вместо turtle
pen = turtle.Pen()
#нужно использовать метод pensize() вместо pen size() потому что в пайтоне не бывает названий или команд с пробелом
pen.pensize(10)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.penup()

pen.color('red', 'yellow')
pen.pendown()
pen.left(90)
pen.forward(100)
pen.left(180)
pen.forward(150)

turtle.done()