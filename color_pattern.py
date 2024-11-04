# Player turtle controls 
import turtle

def move_forward():
    player.forward(10) #when up arrow key is pressed, turtle moves 10 units forward

def turn_left():
    player.left(90) #when left arrow key is pressed, turtle rotates 90 degrees clockwise

def turn_right():
    player.right(90) #when right arrow key is pressed, turtle rotates 90 degrees counter-clockwise

player = turtle.Turtle()
player.shape("turtle")
player.penup()
player.goto(-210, 255) # turtle starting coordinates

scr = turtle.Screen()
scr.listen()
scr.onkey(move_forward, "Up")
scr.onkey(turn_left, "Left")
scr.onkey(turn_right, "Right")

turtle.mainloop()

# Function to display the message
def display_message():
    message_turtle = turtle.Turtle()
    message_turtle.hideturtle()
    message_turtle.penup()
    message_turtle.goto(0, 0) 
    message_turtle.write("Congratulations! You've reached the end!")

# To check if the player reached the end
def check_end():
    if player.distance(230,-270) < 10: 
        display_message()

while True:
    check_end()

turtle.mainloop()
