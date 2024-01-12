from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Ariel', 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as score:
            self.highscore = int(score.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(x=0, y=280)
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as score:
                score.write(str(self.highscore))
        self.score = 0

    def update_score(self):
        self.score += 1
        self.print_score()