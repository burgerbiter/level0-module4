"""
Use boolean variables to control program logic between two different code
paths.
"""
import turtle

if __name__ == '__main__':
    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    weekend = True
    passed = False
    game = True
    color = True
    shape = True

    if weekend:
        print("It's the weekend!")
    else:
        print("Time for school.")
    if passed:
        print("Good job!")
    else:
        print("nice try.")
    if game:
        print("Game Over")
    if color and shape:
        tat = turtle.Turtle()
        tat.pencolor('red')
        for i in range(4):
            tat.forward(100)
            tat.left(90)


    pass
