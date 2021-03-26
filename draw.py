import pygame
import random

pygame.init()

win = pygame.display.set_mode((1000,668))

bg = pygame.image.load('space.jpg')
ufo_img = pygame.image.load('ufo.png')
spaceship_img = pygame.image.load('spaceship.png')
bullet_img = pygame.image.load('bullet.png')
ufo_missile_img = pygame.image.load('missile.png')
music = pygame.mixer.music.load('av_music.mp3')
pygame.mixer.music.play(-1)
bulletSound = pygame.mixer.Sound('awm_s.wav')

pygame.display.set_caption("Space War")
game_icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(game_icon)

run = True
space_x=480
space_y=600
space_vel=3
ufo_x=random.randrange(0,421,4)
ufo_x1=random.randrange(0,21,3)
ufo_y=10
ufo_vel=2
ufo_vel1=3
facing=1
facing1=1
bullet_vel = 5
bullet_state = "ready"
bullet_x = space_x
bullet_y = space_y
missile_x = ufo_x
missile_y = ufo_y
missile_x1 = ufo_x1
missile_y1 = ufo_y 
missile_vel = 4
missile_state = "ready1"
missile_state1 = "ready2"
score = 0
font = pygame.font.SysFont('comicsans', 30, True)

def redrawwindow():
	win.blit(bg,(0,0))
	text = font.render('Score: ' + str(score), 1, (255,0,0))
	win.blit(text, (10, 10))
	win.blit(spaceship_img,(space_x,space_y))
	win.blit(ufo_img,(ufo_x,ufo_y))
	win.blit(ufo_img,(ufo_x1,ufo_y))
	#pygame.draw.rect(win, (255,0,0), spaceship_hitbox,2)
	#pygame.draw.rect(win, (255,0,0), ufo_hitbox,2)

	if bullet_state=="fireing":
		win.blit(bullet_img,(bullet_x,bullet_y))
		#pygame.draw.rect(win, (0,255,0), bullet_hitbox, 2)
	if missile_state == "fire":
		#pygame.draw.rect(win, (0,255,0), missle_hitbox, 2)
		win.blit(ufo_missile_img,(missile_x,missile_y))

	if missile_state1 == "fire2":
		#pygame.draw.rect(win, (0,255,0), missle_hitbox, 2)
		win.blit(ufo_missile_img,(missile_x1,missile_y1))

	pygame.display.update()

while run:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False

	if ufo_x == 900 :
		facing = -1
	elif ufo_x == 152:
		facing = 1
	ufo_x += facing*ufo_vel
	
	if ufo_x1 == 900 :
		facing1 = -1
	elif ufo_x1 == 18:
		facing1 = 1
	ufo_x1 += facing1*ufo_vel1

	if missile_state == "ready1":
		missile_x = ufo_x
		missile_y = ufo_y
		missile_state = "fire"
	if missile_state == "fire":
		if missile_y>0 and missile_y<668:
			missile_y += missile_vel
		else:
			missile_state = "ready1"
	
	if missile_state1 == "ready2":
		missile_x1 = ufo_x1
		missile_y1 = ufo_y
		missile_state1 = "fire2"
	if missile_state1 == "fire2":
		if missile_y1>0 and missile_y1<668:
			missile_y1 += missile_vel
		else:
			missile_state1 = "ready2"

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and space_x > space_vel:
		space_x -= space_vel

	elif keys[pygame.K_RIGHT] and space_x < 1000 - 64 - space_vel:
		space_x += space_vel

	if keys[pygame.K_SPACE]:
		if bullet_state=="ready":
			bulletSound.play()
			bullet_x = space_x
			bullet_y = space_y
			bullet_state="fireing"

	if bullet_state=="fireing":
		if bullet_y>0 and bullet_y<668:
			bullet_y -= bullet_vel
			
		else:
			bullet_state = "ready"

	if bullet_state=="ready":
			bullet_x = space_x
			bullet_y = space_y

	spaceship_hitbox = (space_x , space_y +10, 64, 54)
	ufo_hitbox = (ufo_x, ufo_y, 64, 50)
	ufo_hitbox1 = (ufo_x1, ufo_y, 64, 50)
	bullet_hitbox = (bullet_x+10, bullet_y, 10, 32)
	missle_hitbox = (missile_x+10,missile_y, 12,32)
	missle_hitbox1 = (missile_x1+10,missile_y1, 12,32)
	
	if missle_hitbox[1]+missle_hitbox[3] > spaceship_hitbox[1] and missle_hitbox[0]+missle_hitbox[2]>spaceship_hitbox[0] and missle_hitbox[0]<spaceship_hitbox[0]+spaceship_hitbox[2] :
		score -= 3
		missile_state = "ready1"
	
	if missle_hitbox1[1]+missle_hitbox1[3] > spaceship_hitbox[1] and missle_hitbox1[0]+missle_hitbox1[2]>spaceship_hitbox[0] and missle_hitbox1[0]<spaceship_hitbox[0]+spaceship_hitbox[2] :
		score -= 3
		missile_state1 = "ready2"

	if bullet_hitbox[1]<ufo_hitbox[1]+ufo_hitbox[3] and ufo_hitbox[0]<bullet_hitbox[0]+bullet_hitbox[2] and ufo_hitbox[0]+ufo_hitbox[2]>bullet_hitbox[0] :
		score +=5
		bullet_state = "ready"

	if bullet_hitbox[1]<ufo_hitbox1[1]+ufo_hitbox1[3] and ufo_hitbox1[0]<bullet_hitbox[0]+bullet_hitbox[2] and ufo_hitbox1[0]+ufo_hitbox1[2]>bullet_hitbox[0] :
		score +=5
		bullet_state = "ready"

	redrawwindow()


