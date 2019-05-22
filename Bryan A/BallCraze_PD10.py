from gamelib import *

game = Game(1400,800, "Ball Craze")

bk = Image("Court.jpg",game)
bk.resizeTo(800,600)

player1 = Image("player1.jpg",game)
player1.ResizeBy(-80)
player1.setSpeed(4,60)


