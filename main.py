from turtle import Screen
from scoreboard import Scoreboard
from gameboard import GameBoard



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Tic Tac Toe")
screen.tracer(0)


scoreboard = Scoreboard()
board=GameBoard()
game_on =  True  #board.game_on

while game_on:
    # print("inside while")
    screen.update()
    screen.listen()
    screen.onscreenclick(board.user_play)

    screen.update()
    if board.is_game_over(0):
        if board.game_on:
            scoreboard.increase_score(0)
            board.set_game_off()
            board.info_gameover(0)
        screen.update()

        # game_on = False
        # board = GameBoard()
        # screen.update()
    else:
        # print("game not over")
        if board.can_ai_play():
            # print(" call AI")
            board.random_play()
            if board.is_game_over(1):
                if board.game_on:
                    scoreboard.increase_score(1)
                    board.set_game_off()
                    board.info_gameover(1)
                screen.update()

# screen.exitonclick()
screen.mainloop()