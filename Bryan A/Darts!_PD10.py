from gamelib import *
game = Game(1400,800,"Darts!")
bk=Image("sky.jpg",game)
bk.resizeTo(800,600)

b1 = Image("b1.png",game)
bk.resizeBy(-40)
b1.setSpeed(4,60)

dart = Image("dart.png",game)
dart.resizeBy(-40)

f = Font (black,60,red,"Impact")

while not game.over:
    game.processInput()

    bk.draw()
    b1.move(True)
    dart.move(True)
