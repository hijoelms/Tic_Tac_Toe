from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.computer_score = 0
        self.color("black")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"Your Score: {self.player_score} Computer Score: {self.computer_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.player_score = 0
        self.computer_score = 0


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self,who):
        if who== 0:
            self.player_score += 1
        else:
            self.computer_score +=1
        self.update_scoreboard()



