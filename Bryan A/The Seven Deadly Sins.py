
#Patch v1.00: improved running speed,added dash ability

from gamelib import *

game = Game(800,600,"The Seven Deadly Sins")

bk = Image ("Boar_Hat_91018.jpg", game)
bk.resizeTo(game.width,game.height)

bk2 = Image ("counter screen.png", game)
bk2.resizeTo(game.width,game.height)
#--------------------------------ANIMATION--------------------------------------
meliodas = Animation ("meliodas lol.png",2,game,68/2,65)
meliodas.y = 500
meliodas.resizeBy(120)

meliodasattack = Animation ( "meliodas atk.png",4,game,225/4,54)
meliodasattack.y = 500
meliodasattack.resizeBy(120)

meliodasmoveright = Animation ( "meliodas actual move.png",6,game,240/6,52)
meliodasmoveright.y = 500
meliodasmoveright.resizeBy(120)

meliodascounter= Image ( "meliodas counter.png",game)
meliodascounter.y = 500
meliodascounter.resizeBy(120)

fight = Animation ( "fight.png",6,game,409/6,89)
fight.y = 500
fight.resizeBy(120)


healthcircle = Image ( "dragon sin emblem.png",game)
healthcircle.y = 100
healthcircle.x = 120
healthcircle.resizeBy(2)

health = Image ( "fine.png",game)
health.y = 100
health.x = 450
health.resizeBy(3)

magic = Image ( "magic bar.png",game)
magic.y = 162
magic.x = 450

hurt = Image ("hurt.png",game)
hurt.y = 100
hurt.x = 450
game.font.shadowColor = red

magicloss = Image ( "magicloss.png",game)
magicloss.y = 162
magicloss.x = 450

dash = Animation ("dash.png",2,game,93/2,48)
dash.y = 500
dash.resizeBy(120)

#----------------------------------SOUND----------------------------------------
Sin = Sound ( "Dragon Sin.wav",1)
swordhit = Sound ( "Sword Hit 9.wav",2)
counter = Sound ( "full counter.wav",3)
swordhit2 = Sound ( "Sword Swing 6.wav",4)
#--------------------------------GAMELOOPS--------------------------------------
while not game.over:
    game.processInput()
    bk2 . draw()
    bk .draw()
    Sin.play()
    game.displayScore(85,95)
    healthcircle.draw()
    meliodas.draw()
    hurt.draw()
    health.draw()
    magicloss.draw()
    magic.draw()
    

    if keys.Pressed [K_LEFT]:
        meliodas.visible = False
        meliodasattack.draw()
        game.score +=10
        swordhit2.play()
        bk.visible = True
        
        
        
   
    if keys.Pressed [K_DOWN]:
        
        meliodas.visible = True
        bk.visible = True
        
    if keys.Pressed [K_RIGHT]:
        meliodas.visible = False
        meliodasmoveright.x += 15
        meliodas.x += 15
        meliodasattack.x += 15
        meliodascounter.x += 15
        dash.x +=15
        meliodasmoveright.draw()
        bk.visible = True

    if keys.Pressed [K_UP]:
        meliodas.visible = False
        swordhit.play()
        meliodascounter.draw()
        magic.visible = True
        
        bk.visible = False

    if keys.Pressed[K_SPACE]:
        meliodas.visible = False
        meliodasmoveright.x += 60
        meliodas.x += 60
        meliodasattack.x += 60
        meliodascounter.x += 60
        dash.draw()
        dash.x +=60
        bk.visible = True
    
        magic.visible = False
        

    







    
        
        

        
        

        


     
     


        
    
        
            
            
           
            
            

    game.update(12)

game.quit()
    

    










