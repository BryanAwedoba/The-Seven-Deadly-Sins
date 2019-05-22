from gamelib import*

game = Game(800,600, "Flappy Bird")

bk = Image("day.png",game)
bk.resizeTo(800,600)

bird = Animation( "bird.png",3,game,32/3,34)

while not game.over:
    game.processInput()
    bk.draw()
    bird.draw()


game.update(30)
