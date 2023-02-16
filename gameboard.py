from turtle import Turtle, Screen
from math import floor
from numpy import array, reshape, fliplr, flipud, linalg, diagonal, where
import numpy as np
from random import randint
from time import sleep
# from scoreboard import Scoreboard

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
BIG_FONT = ("Courier", 40, "normal")
sy_array = array([[9,9,9], [9,9,9], [9,9,9]])
# sy_array = array([['', '', ''], ['', '', ''], ['', '', '']])

class GameBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(0, 0)
        self.hideturtle()
        self.draw_board()
        self.lower_x=-225
        self.lower_y=-225
        self.upper_x = -225
        self.upper_y = 225
        global sy_array
        self.matrix_symbol=reshape(sy_array,(3,3))
        # self.score = Scoreboard()
        self.is_user_turn= True
        self.game_on = True
        self.write_reset()

    def draw_board(self):
        x =-225
        y =-225
        for _ in range(0,2):
            x += 150
            self.goto(x, y)
            self.pensize(1)
            self.pendown()
            self.pencolor("black")
            self.setheading(90)
            self.forward(450)
            self.penup()

        x = -225
        y = -225
        for _ in range(0,2):
            y += 150
            self.goto(x, y)
            self.pendown()
            self.pencolor("black")
            self.setheading(0)
            self.forward(450)
            self.penup()


    def draw_symbol(self, x, y):
        # print(x, y)
        RADIUS = 25
        CURSOR_RADIUS = 7
        if x>-225 and x<225 and y>-225 and y<225:
            click_x=floor(abs((self.upper_x - x)/150))
            click_y=floor(abs((self.upper_y - y)/150))
            # print(click_x, click_y)
            segment_x = self.upper_x + 75 + (click_x*150)
            segment_y = self.upper_y - 75 - (click_y * 150)
            # print(segment_x,segment_y)
            if self.matrix_symbol[click_y][click_x]== 9:
                self.matrix_symbol[click_y][click_x] = 0
                self.speed('normal')
                self.penup()
                self.goto(segment_x,segment_y)
                self.shape('circle')
                self.pencolor("black")
                self.fillcolor('white')
                self.shapesize(RADIUS / CURSOR_RADIUS, outline=RADIUS / 7)
                self.stamp()
                self.is_user_turn=False

                # if self.is_game_over(0):
                #     print("Game over, player won")
                #     self.score.increase_score(0)
                # else:
                #     self.random_play()
        elif x > -100 and x < 100 and y > -290 and y < 260:
            self.reset_board(x, y)

    def user_play(self, x,y):
        # print("user_play", x, y )
        if self.game_on:
            self.draw_symbol(x,y)
        else:
            if x > -100 and x < 100 and y > -290 and y < 260:
                self.reset_board(x, y)


    def random_play(self):
        # sleep(1)
        # print(self.matrix_symbol )
        try:

            y_cordlist = np.where(self.matrix_symbol==9)[1]
            x_cordlist = np.where(self.matrix_symbol==9)[0]
            # print("x_cordlist", x_cordlist)
            # print("y_cordlist", y_cordlist)
            t_no = len(x_cordlist)-1
            random_no=randint(0,t_no)
            # print("9s in this location:", np.where(self.matrix_symbol==9))
            y_cord= y_cordlist[random_no]
            x_cord= x_cordlist[random_no]
            # print("y_cord:", y_cord)
            # print("x_cord:",x_cord)
            # print("random_no",random_no, x_cord, y_cord)
            segment_x = self.upper_x + 75 + (y_cord * 150)
            segment_y = self.upper_y - 75 - (x_cord * 150)
            # print("segment_x:", segment_x)
            # print("segment_y:", segment_y)
            self.speed(0)
            self.matrix_symbol[x_cord][y_cord] = 1
            self.penup()
            self.pensize(5)
            self.goto(segment_x, segment_y)
            self.shape('square')
            self.shapesize(stretch_wid=.1, stretch_len=.1,outline=None)
            self.pencolor("red")
            self.fillcolor('red')
            RADIUS = 25
            CURSOR_RADIUS = 7
            # self.shapesize(RADIUS / CURSOR_RADIUS, outline=RADIUS / 7)
            self.setheading(45)
            self.pendown()
            self.forward(50)
            # self.showturtle()
            self.hideturtle()
            self.penup()
            self.goto(segment_x, segment_y)
            self.setheading(225)
            self.pendown()
            self.forward(50)
            self.penup()
            self.goto(segment_x, segment_y)
            self.setheading(135)
            self.pendown()
            self.forward(50)
            self.penup()
            self.goto(segment_x, segment_y)
            self.setheading(315)
            self.pendown()
            self.forward(50)
            self.penup()
            self.goto(segment_x, segment_y)
            self.stamp()
            self.is_user_turn = True
            # if self.is_game_over(1):
            #     print("Game over, Computer won")
            #     self.score.increase_score(1)
        except:
            # print("Game draw")
            self.info_gameover(3)
            pass

    def can_ai_play(self):
        return not self.is_user_turn


    def draw_strike(self,how,no):
        if how=="Row":
            drawing=False
            for i in range(3):
                segment_x = self.upper_x + 75 + (i * 150)
                segment_y = self.upper_y - 75 - (no * 150)
                # print(segment_x, segment_y)
                if not drawing:
                    self.penup()
                    self.setheading(0)
                    self.pensize(5)
                    self.goto(segment_x, segment_y)
                    self.shape('square')
                    self.shapesize(stretch_wid=.1, stretch_len=.1, outline=None)
                    self.pencolor("black")
                    self.fillcolor('black')
                    drawing=True
                else:

                    self.pendown()
                    self.goto(segment_x, segment_y)
                    # self.showturtle()
                    self.hideturtle()
                    self.penup()

        elif how=="Column":
            drawing = False
            for i in range(3):
                segment_x = self.upper_x + 75 + (no * 150)
                segment_y = self.upper_y - 75 - (i * 150)
                # print(segment_x, segment_y)
                if not drawing:
                    self.penup()
                    self.setheading(0)
                    self.pensize(5)
                    self.goto(segment_x, segment_y)
                    self.shape('square')
                    self.shapesize(stretch_wid=.1, stretch_len=.1, outline=None)
                    self.pencolor("black")
                    self.fillcolor('black')
                    drawing = True
                else:

                    self.pendown()
                    self.goto(segment_x, segment_y)
                    # self.showturtle()
                    self.hideturtle()
                    self.penup()
        elif how == "Diagonal 1":
            segment_x = self.upper_x + 75 + (0 * 150)
            segment_y = self.upper_y - 75 - (0 * 150)
            # print(segment_x, segment_y)

            self.penup()
            self.setheading(315)
            self.pensize(5)
            self.goto(segment_x, segment_y)
            self.shape('square')
            self.shapesize(stretch_wid=.1, stretch_len=.1, outline=None)
            self.pencolor("black")
            self.fillcolor('black')
            segment_x = self.upper_x + 75 + (1 * 150)
            segment_y = self.upper_y - 75 - (1 * 150)
            # print(segment_x, segment_y)
            self.pendown()
            self.goto(segment_x, segment_y)
            # self.showturtle()
            self.hideturtle()
            self.penup()
            segment_x = self.upper_x + 75 + (2 * 150)
            segment_y = self.upper_y - 75 - (2 * 150)
            # print(segment_x, segment_y)
            self.pendown()
            self.goto(segment_x, segment_y)
            # self.showturtle()
            self.hideturtle()
            self.penup()
        elif how == "Diagonal 2":
            segment_x = self.upper_x + 75 + (0 * 150)
            segment_y = self.upper_y - 75 - (2 * 150)
            # print(segment_x, segment_y)

            self.penup()
            self.setheading(315)
            self.pensize(5)
            self.goto(segment_x, segment_y)
            self.shape('square')
            self.shapesize(stretch_wid=.1, stretch_len=.1, outline=None)
            self.pencolor("black")
            self.fillcolor('black')
            segment_x = self.upper_x + 75 + (1 * 150)
            segment_y = self.upper_y - 75 - (1 * 150)
            # print(segment_x, segment_y)
            self.pendown()
            self.goto(segment_x, segment_y)
            # self.showturtle()
            self.hideturtle()
            self.penup()
            segment_x = self.upper_x + 75 + (2 * 150)
            segment_y = self.upper_y - 75 - (0 * 150)
            # print(segment_x, segment_y)
            self.pendown()
            self.goto(segment_x, segment_y)
            # self.showturtle()
            self.hideturtle()
            self.penup()

    def is_game_over(self, player_no):
        # print(self.matrix_symbol)
        # print(np.matrix.transpose (self.matrix_symbol))
        # print("Column count:", 3 in (self.matrix_symbol == player_no).sum(axis=1))
        # print("Row count:", 3 in (self.matrix_symbol == player_no).sum(axis=0))
        # print(self.matrix_symbol.diagonal())
        # print(fliplr(self.matrix_symbol).diagonal())
        # print("Bottom to up left to right", (self.matrix_symbol == player_no).diagonal().sum(axis=0))
        # print("Top to bottom left to right", fliplr(self.matrix_symbol == player_no).diagonal().sum(axis=0))
        if 3 in (self.matrix_symbol == player_no).sum(axis=1): # Row count
            # print("Row count:", (self.matrix_symbol == player_no).sum(axis=1))
            row_no=np.where((self.matrix_symbol == player_no).sum(axis=1)==3)[0][0]
            # print("Row no:",row_no )
            self.draw_strike("Row", row_no)
            return True
        elif 3 in (self.matrix_symbol == player_no).sum(axis=0): # Column count
            # print("Column count:",(self.matrix_symbol == player_no).sum(axis=0))
            column_no=np.where((self.matrix_symbol == player_no).sum(axis=0)==3)[0][0]
            # print("Column no:", column_no)
            self.draw_strike("Column", column_no)
            return True
        elif (self.matrix_symbol == player_no).diagonal().sum(axis=0)==3: # Bottom to up left to right
            # print("Diagonal 1:", (self.matrix_symbol == player_no).diagonal().sum(axis=0))
            self.draw_strike("Diagonal 1", 0)
            return True
        elif fliplr(self.matrix_symbol == player_no).diagonal().sum(axis=0)==3: # Top to bottom left to right
            # print("Diagonal 2:", fliplr(self.matrix_symbol == player_no).diagonal())
            self.draw_strike("Diagonal 2", 0)
            return True
        else:
            self.game_on = True
            return False

    def reset_board(self, x, y):
        # print(x, y)
        if x > -80 and x < 70 and y > -260 and y < -240:
            RADIUS = 60
            CURSOR_RADIUS = 7
            y_cordlist = np.where(self.matrix_symbol != 9)[1]
            x_cordlist = np.where(self.matrix_symbol != 9)[0]
            t_no = len(x_cordlist)
            # random_no = randint(0, t_no)
            for i in range(t_no):
                y_cord = y_cordlist[i]
                x_cord = x_cordlist[i]
                # print("y_cord:", y_cord)
                # print("x_cord:",x_cord)
                # print("random_no", i, x_cord, y_cord)
                segment_x = self.upper_x + 75 + (y_cord * 150)
                segment_y = self.upper_y - 75 - (x_cord * 150)
                # print("segment_x:", segment_x)
                # print("segment_y:", segment_y)
                self.speed('normal')
                self.penup()
                self.goto(segment_x, segment_y)
                self.shape('circle')
                self.pencolor("white")
                self.fillcolor('white')
                self.shapesize(RADIUS / CURSOR_RADIUS, outline=RADIUS / 7)
                self.stamp()
                self.matrix_symbol[x_cord][y_cord] = 9

            self.reset_all_board()
            self.draw_board()
            self.is_user_turn = True
            self.game_on = True

    def reset_all_board(self):
        RADIUS = 120
        CURSOR_RADIUS = 7
        self.speed('normal')
        self.penup()
        self.goto(0, 0)
        self.shape('circle')
        self.pencolor("white")
        self.fillcolor('white')
        self.shapesize(RADIUS / CURSOR_RADIUS, outline=RADIUS / 7)
        self.stamp()

    def game_on(self):
        return self.game_on

    def set_game_off(self):
        self.game_on= False

    def info_gameover(self, user):
        self.goto(0, 25)
        self.pencolor("blue")
        if user==0:
            self.write("You won", align=ALIGNMENT, font=BIG_FONT)
        elif user==1:
            self.write("Computer won", align=ALIGNMENT, font=BIG_FONT)
        else:
            self.write("Game is draw", align=ALIGNMENT, font=BIG_FONT)

    def write_reset(self):
        # self.clear()
        self.goto(0, -270)
        self.write("Reset Game", align=ALIGNMENT, font=FONT)
