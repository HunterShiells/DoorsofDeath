import pygame as game
import random as r

#--------------------------------------initiation--------------------------------------
game.mixer.pre_init(44100, -16, 2, 2048)
game.mixer.init()
game.init()
game.mixer.music.load("Assets/Fantasy-Forest-Battle.wav")
chestmsc = game.mixer.Sound("Assets/Powerup6.wav")
shootmsc = game.mixer.Sound("Assets/Laser_Shoot4.wav")
piratemsc = game.mixer.Sound("Assets/Explosion4.wav")
game.display.set_caption("The Door of Death")
screen = game.display.set_mode([640,480])
gameon = True
#---------------------------------------Variables--------------------------------
blue = game.color.Color("#0f70ad")
grey = game.color.Color("#9d9ea0")
gold = game.color.Color("#DAA520")
black = game.color.Color("#000000")
red = game.color.Color("#ff0000")
bg1 = game.image.load("Assets/bg1.png")
bg2 = game.image.load("Assets/bg2.png")
bg3 = game.image.load("Assets/bg3.png")
bg4 = game.image.load("Assets/bg4.png")
bg5 = game.image.load("Assets/bg5.png")
bg6 = game.image.load("Assets/bg6.png")
player1 = game.image.load("Assets/person.png")
pleft = game.image.load("Assets/personleft.png")
pright = game.image.load("Assets/personright.png")
pshoot = game.image.load("Assets/personshooting.png")
pshootr = game.image.load("Assets/personshootingright.png")
pshootl = game.image.load("Assets/personshootingleft.png")
chest = game.image.load("Assets/chest.png")
bull = game.image.load("Assets/bullet.png")
bulls = game.image.load("Assets/bullet.png")
go = game.image.load("Assets/gameover.png")
mouse = game.image.load("Assets/mouse.png")
heart = game.image.load("Assets/heart.png")
pirate = game.image.load("Assets/pirate.png")
plottxt = game.image.load("Assets/plot.png")
island = game.image.load("Assets/island.png")
player1img = player1
topright = game.Rect(350,0,285,45)
topleft = game.Rect(0,0,290,45)
top = game.Rect(0,0,640,45)
right = game.Rect(590,0,48,480)
righttop = game.Rect(590,0,48,207)
rightbottom = game.Rect(590,270,48,210)
left = game.Rect(0,0,50,480)
lefttop = game.Rect(0,0,50,208)
leftbottom = game.Rect(0,272,50,208)
bottom = game.Rect(0,435,640,45)
bottomright = game.Rect(350,435,290,45)
bottomleft = game.Rect(0,435,287,45)
doorbg1 = game.Rect(285,0,45,65)
doorbg2 = game.Rect(590,207,45,65)
doorbg3 = game.Rect(287,435,65,45)
doorbg4 = game.Rect(0,208,50,65)
trp1 = game.Rect(47,45,240,165)
trp2 = game.Rect(416,45,177,75)
trp3 = game.Rect(285,115,75,95)
trp4 = game.Rect(531,115,62,320)
trp5 = game.Rect(360,182,115,100)
trp6 = game.Rect(300,340,290,95)
trp7 = game.Rect(205,265,100,170)
trp8 = game.Rect(100,165,50,215)
prect = game.Rect(50,45,110,390)
font = game.font.Font(None,30)
guntxt = font.render("", 0, gold)
nogun = font.render("You did not find the gun! Click to Quit.", 0, red)
enttxt = font.render("", 0, red)
rmtxt = font.render("", 0, red)
youtxt = font.render("You: ", 0, black)
pirtxt = font.render("Pirate: ", 0, red)
movement = 2
#---------------------------------------Legs moving--------------------------------

p1count=0
p1 = [100,100]
pir1 = [50,200]
bullets = []
pirs  = []
SPAWNENEMY = 10
game.time.set_timer(SPAWNENEMY,550)
SPAWNBULLET = 10
game.time.set_timer(SPAWNBULLET,450)
mouses = []
hearts = [[50,12.5],[72,12.5],[94,12.5],[116,12.5],[138,12.5],[160,12.5],[182,12.5],
          [204,12.5],[226,12.5],[248,12.5]]
heartsnum = 10
prhearts = [[400,445],[422,445],[444,445],[466,445],[488,445],[510,445],[532,445],
           [554,445],[576,445],[598,445]]
prhearsnum = 15
mum = 0
def p1img():
    global p1count, player1img, pleft, pright
    p1count +=1
    if p1count==8:
        p1count = 0
        if player1img==pleft:
            player1img=pright
        else:
            player1img=pleft
#---------------------------------------Plot----------------------------------------------------
plot = True
while plot:
    screen.blit(plottxt,(0,0))
    game.display.flip()
    event = game.event.poll()
    if event.type == game.MOUSEBUTTONDOWN:
        break
#---------------------------------------Intro Screen-----------------------------
logo = game.image.load("intro/logo.png")
gamefont = game.font.Font(None,30)
gamestart = gamefont.render("Click screen to begin", 0, gold)
#---------------------------------------------------------------------------------------
intro = True
while intro:
    screen.blit(bg1, (0,0))
    screen.blit(gamestart, (215,300))
    screen.blit(logo, (125,50))
    game.display.flip()
    event = game.event.poll()
    if event.type == game.MOUSEBUTTONDOWN:
        break
#---------------------------------------Game Starting-----------------------------------
game.mixer.music.play(-1)
gameon = True
while gameon:
    screen.blit(bg1,(0,0))
    screen.blit(player1img,p1)
    screen.blit(youtxt, (5,12.5))
    for hg in hearts: 
        screen.blit(heart,hg)
    game.display.flip()
    parea = game.Rect(player1.get_rect())
    parea.x = p1[0]
    parea.y = p1[1]
    keys = game.key.get_pressed()
    if keys[game.K_d] and right.colliderect(parea)==False:
        p1[0] +=2
        p1img()
    elif keys[game.K_a] and left.colliderect(parea)==False:
        p1[0] -=2
        p1img()
    elif keys[game.K_w] and topleft.colliderect(parea)==False and topright.colliderect(parea)==False:
        p1[1] -=2
        p1img()
        if doorbg1.colliderect(parea):
            break
    elif keys[game.K_s] and bottom.colliderect(parea)==False:
        p1[1] +=2
        p1img()
    else:
        player1img = player1
    event=game.event.poll()
    if event.type == game.QUIT:
        game.quit()

secondon = True
p1 = [310,390]
while secondon:
    screen.blit(bg2,(0,0))
    screen.blit(chest,(270,45))
    screen.blit(player1img,p1)
    screen.blit(guntxt,(110,400))
    screen.blit(enttxt,(125,400))
    screen.blit(youtxt, (5,12.5))
    for hg in hearts: 
        screen.blit(heart,hg)
    parea = game.Rect(player1.get_rect())
    recchest = game.Rect(270,45,100,55)
    parea.x = p1[0]
    parea.y = p1[1]
    keys = game.key.get_pressed()
    if keys[game.K_d] and righttop.colliderect(parea)==False and rightbottom.colliderect(parea)==False:
        p1[0] +=2
        p1img()
        if doorbg2.colliderect(parea):
            guntxt = font.render("", 0, gold)
            enttxt = font.render("Killer Mouses!!! survive or kill them!", 0, red)
            if player1 == pshoot or pleft == pshootl or pright == pshootr:
                break
            elif player1img == pleft or player1img == pright:
                screen.blit(go, (200,100))
                screen.blit(nogun,(140,300))
                game.display.flip()
                game.event.poll()
                while True:
                    event=game.event.poll()
                    if event.type == game.MOUSEBUTTONDOWN:
                        game.quit()
    elif keys[game.K_a] and left.colliderect(parea)==False:
        p1[0] -=2
        p1img()
    elif keys[game.K_w] and top.colliderect(parea)==False:
        p1[1] -=2
        p1img()
        if recchest.colliderect(parea):
            chestmsc.play()
            guntxt = font.render("You picked up the gun! LeftClick to shoot!!!", 0, gold)
            player1 = pshoot
            pleft = pshootl
            pright = pshootr
    elif keys[game.K_s] and bottom.colliderect(parea)==False:
        p1[1] +=2
        p1img()
    else:
        player1img = player1

    parea = game.Rect(player1.get_rect())
    parea.x = p1[0]
    parea.y = p1[1]
    if player1 == pshoot or pleft == pshootl or pright == pshootr:
        if event.type==game.MOUSEBUTTONDOWN:
            shootmsc.play()
            mx,my = game.mouse.get_pos()
            bulletx = p1[0] + 15
            bullety = p1[1] + 15
            cx = (mx - bulletx) / 40 * (640/480)
            cy = (my - bullety) / 40 * (640/480)
            if (cx == 0 and cy ==0):
                cx=3
                cy=0
            bullets.append([bulletx, bullety, cx, cy])
        for bullet in bullets:
            bullet[0] += bullet[2]
            bullet[1] += bullet[3]
            if bullet[0] > 582:
                bullets.remove(bullet)
            elif bullet[0] < 35:
                bullets.remove(bullet)
            if bullet[1] > 435:
                bullets.remove(bullet)
            elif bullet[1] < 45:
                bullets.remove(bullet)
            
        for bullet in bullets:
            screen.blit(bull, bullet)
  
    game.display.flip()    
    event=game.event.poll()
    if event.type == game.QUIT:
        game.quit()

thirdon = True

p1 = [50,215]
while thirdon:
    screen.blit(bg3,(0,0))
    screen.blit(player1img,p1)
    screen.blit(enttxt,(145,400))
    screen.blit(rmtxt,(115,435))
    screen.blit(youtxt, (5,12.5))
    for hg in hearts: 
        screen.blit(heart,hg)
    parea = game.Rect(player1.get_rect())
    parea.x = p1[0]
    parea.y = p1[1]
    keys = game.key.get_pressed()
    if keys[game.K_d] and right.colliderect(parea)==False:
        p1[0] +=2
        p1img()
    elif keys[game.K_a] and left.colliderect(parea)==False:
        p1[0] -=2
        p1img()
    elif keys[game.K_w] and top.colliderect(parea)==False:
        p1[1] -=2
        p1img()
    elif keys[game.K_s] and bottomleft.colliderect(parea)==False and bottomright.colliderect(parea)==False:
        p1[1] +=2
        p1img()
        if mum == 25:
            if doorbg3.colliderect(parea):
                break
    else:
        player1img = player1
    parea = game.Rect(player1.get_rect())
    parea.x = p1[0]
    parea.y = p1[1]
    if player1 == pshoot or pleft == pshootl or pright == pshootr:
        if event.type==game.MOUSEBUTTONDOWN:
            shootmsc.play()
            mx,my = game.mouse.get_pos()
            bulletx = p1[0] + 15
            bullety = p1[1] + 15
            cx = (mx - bulletx) / 50 * (640/480)
            cy = (my - bullety) / 50 * (640/480)
            if (cx == 0 and cy ==0):
                cx=3
                cy=0
            bullets.append([bulletx, bullety, cx, cy])
        for bullet in bullets:
            bullet[0] += bullet[2]
            bullet[1] += bullet[3]
            screen.blit(bull, bullet)
            bulletarea = game.Rect(bull.get_rect())
            bulletarea.x = bullet[0]
            bulletarea.y = bullet[1]
            for bg in mouses:
                bgarea = game.Rect(mouse.get_rect())
                bgarea.x = bg[0]
                bgarea.y = bg[1]
                if bgarea.colliderect(bulletarea):
                    bullets.remove(bullet)
                    mouses.remove(bg)
        if(len(bullets) > 15):
            bullets.pop(0)
        if event.type == SPAWNENEMY and mum < 25:
            mum += 1
            mouses.append([580,r.randrange(50,400)])
        for bg in mouses:
            bg[0] -= 2.5
        for bg in mouses:
            screen.blit(mouse,bg)
            bgarea = game.Rect(mouse.get_rect())
            bgarea.x = bg[0]
            bgarea.y = bg[1]
            if bgarea.colliderect(parea):
                hearts.pop()
                p1 = [50,215]
                if len(hearts)==0:
                   screen.blit(go, (200,50))
                   game.display.flip()
                   game.quit()
    if mum == 25:
        enttxt = font.render("", 0, red)
        rmtxt = font.render("Go slow into the next door. You feel a brease", 0, red)           
            
    game.display.flip()
    event=game.event.poll()
    if event.type == game.QUIT:
        game.quit()

fourthon = True
p1 = [300,15]
while fourthon:
    screen.blit(bg4,(0,0))
    game.draw.rect(screen,black,trp1)
    game.draw.rect(screen,black,trp2)
    game.draw.rect(screen,black,trp3)
    game.draw.rect(screen,black,trp4)
    game.draw.rect(screen,black,trp5)
    game.draw.rect(screen,black,trp6)
    game.draw.rect(screen,black,trp7)
    game.draw.rect(screen,black,trp8)
    screen.blit(rmtxt,(115,435))
    screen.blit(youtxt, (5,12.5))
    rmtxt = font.render("The floor has fallen watch your STEP!", 0, red)
    for hg in hearts: 
        screen.blit(heart,hg)
    player1imgg = game.transform.flip(player1img, True, False)
    screen.blit(player1imgg,p1)
    parea = game.Rect(player1.get_rect())
    parea.x = p1[0]
    parea.y = p1[1]
    keys = game.key.get_pressed()
    if keys[game.K_d] and right.colliderect(parea)==False:
        p1[0] +=2
        p1img()
    elif keys[game.K_a] and lefttop.colliderect(parea)==False and leftbottom.colliderect(parea)==False:
        p1[0] -=2
        p1img()
        if doorbg4.colliderect(parea):
            break
    elif keys[game.K_w] and top.colliderect(parea)==False:
        p1[1] -=2
        p1img()
    elif keys[game.K_s] and bottom.colliderect(parea)==False:
        p1[1] +=2
        p1img()
    else:
        player1img = player1

    parea = game.Rect(player1.get_rect())
    parea.x = p1[0]
    parea.y = p1[1]
    if player1 == pshoot or pleft == pshootl or pright == pshootr:
        if event.type==game.MOUSEBUTTONDOWN:
            shootmsc.play()
            mx,my = game.mouse.get_pos()
            bulletx = p1[0] + 15
            bullety = p1[1] + 15
            cx = (mx - bulletx) / 50 * (640/480)
            cy = (my - bullety) / 50 * (640/480)
            if (cx == 0 and cy ==0):
                cx=3
                cy=0
            bullets.append([bulletx, bullety, cx, cy])
        for bullet in bullets:
            bullet[0] += bullet[2]
            bullet[1] += bullet[3]
        if(len(bullets) > 15):
            bullets.pop(0) 
        for bullet in bullets:
            screen.blit(bull, bullet)
    if trp1.colliderect(parea):
        hearts.pop()
        p1 = [300,45]
        if len(hearts)==0:
            screen.blit(go, (200,50))
            game.display.flip()
            game.quit()
    if trp2.colliderect(parea):
        hearts.pop()
        p1 = [300,45]
        if len(hearts)==0:
           screen.blit(go, (200,50))
           game.display.flip()
           game.quit()
    if trp3.colliderect(parea):
        hearts.pop()
        p1 = [300,45]
        if len(hearts)==0:
           screen.blit(go, (200,50))
           game.display.flip()
           game.quit()
    if trp4.colliderect(parea):
        hearts.pop()
        p1 = [300,45]
        if len(hearts)==0:
           screen.blit(go, (200,50))
           game.display.flip()
           game.quit()
    if trp5.colliderect(parea):
        hearts.pop()
        p1 = [300,45]
        if len(hearts)==0:
           screen.blit(go, (200,50))
           game.display.flip()
           game.quit()
    if trp6.colliderect(parea):
        hearts.pop()
        p1 = [300,45]
        if len(hearts)==0:
           screen.blit(go, (200,50))
           game.display.flip()
           game.quit()
    if trp7.colliderect(parea):
        hearts.pop()
        p1 = [300,45]
        if len(hearts)==0:
           screen.blit(go, (200,50))
           game.display.flip()
           game.quit()
    if trp8.colliderect(parea):
        hearts.pop()
        p1 = [300,45]
        if len(hearts)==0:
           screen.blit(go, (200,50))
           game.display.flip()
           game.quit()
            
    game.display.flip()
    event=game.event.poll()
    if event.type == game.QUIT:
        game.quit()

fifthon = True
p1 = [560,215]
while fifthon:
    screen.blit(bg6,(0,0))
    pirate2 = game.transform.flip(pirate, True, False)
    screen.blit(pirate2, pir1)
    screen.blit(youtxt, (5,12.5))
    screen.blit(pirtxt, (335,445))
    for hg in hearts: 
        screen.blit(heart,hg)
    for phg in prhearts: 
        screen.blit(heart,phg)
    player1imgg = game.transform.flip(player1img, True, False)
    screen.blit(player1imgg,p1)
    parea = game.Rect(player1.get_rect())
    parea.x = p1[0]
    parea.y = p1[1]
    keys = game.key.get_pressed()
    if keys[game.K_d] and right.colliderect(parea)==False:
        p1[0] +=2
        p1img()
    elif keys[game.K_a] and left.colliderect(parea)==False and prect.colliderect(parea)==False:
        p1[0] -=2
        p1img()
    elif keys[game.K_w] and top.colliderect(parea)==False:
        p1[1] -=2
        p1img()
    elif keys[game.K_s] and bottom.colliderect(parea)==False:
        p1[1] +=2
        p1img()
    else:
        player1img = player1

    parea = game.Rect(player1.get_rect())
    parea.x = p1[0]
    parea.y = p1[1]
    if player1 == pshoot or pleft == pshootl or pright == pshootr:
        if event.type==game.MOUSEBUTTONDOWN:
            shootmsc.play()
            mx,my = game.mouse.get_pos()
            bulletx = p1[0] + 15
            bullety = p1[1] + 15
            cx = (mx - bulletx) / 50 * (640/480)
            cy = (my - bullety) / 50 * (640/480)
            if (cx == 0 and cy ==0):
                cx=3
                cy=0
            bullets.append([bulletx, bullety, cx, cy])
        for bullet in bullets:
            bullet[0] += bullet[2]
            bullet[1] += bullet[3]
        if(len(bullets) > 15):
            bullets.pop(0) 
        for bullet in bullets:
            screen.blit(bull, bullet)
            bulletarea = game.Rect(bull.get_rect())
            bulletarea.x = bullet[0]
            bulletarea.y = bullet[1]
            pirarea = game.Rect(pirate2.get_rect())
            pirarea.x = pir1[0]
            pirarea.y = pir1[1]
            if bulletarea.colliderect(pirarea):
                prhearts.pop()
                bullets.remove(bullet)
    if len(hearts)==0:
        break
    pirarea = game.Rect(pirate2.get_rect())
    pirarea.x = pir1[0]
    pirarea.y = pir1[1]
    if event.type == SPAWNBULLET:
        piratemsc.play()
        pirx = pir1[0] + 100
        piry = pir1[1] + 25
        pirs.append([pirx, piry])    
    for pr in pirs:
        pr[0] += 1
        screen.blit(bulls, pr)
        bullsarea = game.Rect(bulls.get_rect())
        bullsarea.x = pr[0]
        bullsarea.y = pr[1]
        if parea.colliderect(bullsarea):
            hearts.pop()
            pirs.remove(pr)
            p1 = [r.randrange(200,590),r.randrange(50,400)]
    if len(prhearts)==0:
        break
    pirarea = game.Rect(pirate2.get_rect())
    pirarea.x = pir1[0]
    pirarea.y = pir1[1]
    if pir1[1] >= 435-60:
        movement = -2
    if pir1[1] <= 50:
        movement = +2
    pir1[1] += movement
    game.display.flip()
    event=game.event.poll()
    if event.type == game.QUIT:
        game.quit()
    

game.mixer.music.stop()
while True:
    screen.blit(island,(0,0))
    screen.blit(go, (200,50))
    screen.blit(rmtxt,(125,400))
    rmtxt = font.render("", 0, gold)
    if len(prhearts) == 0:
            rmtxt = font.render("You defeated the final boss. You're FREE!", 0, gold)
    if len(hearts) == 0:
        rmtxt = font.render("The Pirate stopped the Escape. Try Again", 0, gold)
    game.display.flip()
    event=game.event.poll()
    if event.type == game.QUIT:
        break
game.quit()
