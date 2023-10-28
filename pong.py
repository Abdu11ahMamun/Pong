import turtle

window = turtle.Screen()
window.title("Pong game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) #stops the window from updating


#Main game loop
while True:
    window.update()
