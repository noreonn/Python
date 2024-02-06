# This is a very simple program about balls, demonstrating Object Orientation in Python

class Ball:
    # Constructor to initialize diameter and colour of the ball
    def __init__(self):
        self.diameter = 0.0
        self.colour = ""

    # Method to make the ball bounce
    def bounce(self):
        if self.diameter > 5:
            print("Big boing when bouncing")
        else:
            print("Boing when bouncing")

    # Method to make the ball roll
    def roll(self):
        print(self.colour,"blur when rolling")

if __name__ == "__main__":
    # Creating a tennis ball object
    tennis_ball = Ball()
    tennis_ball.diameter = 5.5
    tennis_ball.colour = "green"

    # Making the tennis ball bounce and roll
    tennis_ball.bounce()
    tennis_ball.roll()

    # Creating a cricket ball object
    cricket_ball = Ball()
    cricket_ball.diameter = 4.2
    cricket_ball.colour = "red"


    # Making the cricket ball bounce and roll
    cricket_ball.bounce()
    cricket_ball.roll()

