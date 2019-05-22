from gamelib import*#import the game library of functions
#objects
game = Game(800,600,"Zombies Attack!")#create a game object

bk = Image("Zbk.jpg",game)#create an image object
bk.resizeTo(800,600)#resize bk to 800,600

turkey = Image("turkey.gif",game)#create an image object
turkey.resizeBy(-50)#resize the turkey
turkey.setSpeed(4,60)

zombie = Image("zombie.png",game)#create an image object
zombie.resizeBy(-80)#resize the zombie
zombie.setSpeed(4,60)

ZombieDie=Sound("ZombieDie.wav",1)

crosshair = Image("crosshair.png",game)
crosshair.resizeBy(-85)

gun=Sound("Gun.wav",1)

while not game.over:#game loop
    game.processInput()

    if crosshair.collidedWith(zombie)and mouse.LeftClick:
        ZombieDie.play()
        
    bk.draw()#bk will draw
    turkey.move(True)#the turkey will draw
    zombie.move(True)#the zombie will draw
    crosshair.moveTo(mouse.x,mouse.y)#the crosshairs will move to the mouse location
    
    if mouse.LeftClick:
        gun.play()
        
    if crosshair.collidedWith(zombie)and mouse.LeftClick:
        game.score+=10#accumulator variable
    game.displayScore()#displays the game score
    game.update(30)#game will update frames per second
    


game.quit()#quit the game












