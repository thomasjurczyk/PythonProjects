from turtle import Turtle

def treeBuilder(branch,turtle):
    if branch > 5:
        turtle.forward(branch)
        turtle.right(20)
        treeBuilder(branch-5,turtle)
        turtle.left(40)
        treeBuilder(branch-5,turtle)
        turtle.right(20)
        turtle.backward(branch)
turtle = Turtle()
turtle.left(90)
turtle.up()
turtle.backward(100)
turtle.down()
turtle.color("blue")
treeBuilder(50,turtle)
