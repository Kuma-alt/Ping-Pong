from pygame import *
#from random import randint
#from time import time as timer

back = (71, 131, 160) 
win_width = 600
win_height = 500
window = display.set_mode((600, 500))
display.set_caption("Пінг-Понг")
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed 
            
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed 

racket1 = Player('racket.jpg', 30, 200, 4, 50, 150)
racket2 = Player('racket.jpg', 30, 200, 4, 50, 150)
ball = GameSprite('ball.jpg', 200, 200, 4, 50, 50)

finish = False
game = True
clock = time.Clock()
FPS = 60

font.init()
font = font.font(None, 35)
lose1 = font.render('PLAYER 1 LOSE', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

     if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
            
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= 1
            
        if ball.rect.x < 0
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True
            
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True
            
        racket1.reset()
        racket2.reset()
        ball.reset()
        
    display.update()
    clock.tick(FPS)
        
'''''
    if not finish:
        window.blit(background, (0, 0))

        text = font2.render("Рахунок: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))

        
        ship.update()
        monsters.update()
        asteroids.update()
        bullets.update()
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
        asteroids.draw(window)

        if rel_time == True:
            now_time = timer()

            if now_time - last_time < 1:
                reload = font2.render('Wait, reload...', 1,(150, 0, 0))
                window.blit(reload, (260, 460))
            else:
                num_fire = 0
                rel_time = False

        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1
            monster = Enemy("ufo.png", randint(80, win_width - 80), -40, randint(1,5))
            monsters.add(monster)
        if sprite.spritecollide(ship, monsters, False) or lost >= 3 :
            finish = True
            window.blit(lose, (200, 200))

        if sprite.spritecollide(ship, asteroids, False):
            finish = True
            window.blit(lose, (200, 200))
            
        if score >= 10:
            finish = True
            window.blit(win, (200, 200))
                
        display.update()

    time.delay(15)
'''''

    
