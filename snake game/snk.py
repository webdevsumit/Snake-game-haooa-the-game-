import pygame
import random
import os
pygame.init()
pygame.mixer.init()

bgmg=pygame.image.load("S_snk.jpg")
bgmg=pygame.transform.scale(bgmg,(720,800))
win = pygame.display.set_mode((800,1300))
pygame.display.set_caption("HAOOA the game")
x = 200
y = 200
w = 25
h = 30
v_x= 3
v_y=0
snk_len=1
score=1
randx=500
randy=400
def res(g,h,i,j):
	pygame.draw.rect(win,(100,25,225),(g,h,i,j))
	
font=pygame.font.Font("Raleway-ExtraBold.ttf", 55)
def text_screen(text,color,p,q):
	screen_text=font.render(text, True, color)
	win.blit(screen_text, (p,q))
	
if (not os.path.exists("highscore.txt")):
	with open("highscore.txt", "w") as f:
		f.write("0")

snk_size=[]
keys = pygame.key.get_pressed()
start = False
pygame.mixer.music.load("9394_pubg_bgm_ringtone_ringtone_mp3.mp3")
pygame.mixer.music.play()
while not start :
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	bgimg=pygame.image.load("Haooa.jpg")
	bgimg=pygame.transform.scale(bgimg,(720,800))
	win.fill((0,0,0))
	win.blit(bgimg,(0,0))
	text_screen("made by sumit",(0,100,100),335,747)
	cur=pygame.mouse.get_pos()
	pygame.draw.rect(win, (0,0,225),(400,480,100,50))
	if 500>cur[0]>400 and 510>cur[1]>480:
		pygame.draw.rect(win, (200,150,0),(400,480,100,50))
		start = True
	pygame.display.update()	
run = True
game_over=False
pygame.mixer.music.load("13724_alan_walker_on_my_way_marimba_remix_ringtone_2019_ringtone_mp3.mp3")
pygame.mixer.music.play(100)
while run:
	with open("highscore.txt", "r") as r:
		highscore=r.read()
	if int(highscore)<((score-1)*10):
		highscore=str((score-1)*10)
	with open("highscore.txt","w") as f:
		f.write(highscore)
	if game_over==True:
		pygame.mixer.music.load("Electric Shock Zap-SoundBible.com-68983399.mp3")
		pygame.mixer.music.play()
		while game_over:
			text_screen("GAME OVER", (25,0,0),200,400)
			text_screen("press resume to restart", (25,0,0),80,450)
			if (score-1)*10==int(highscore):
				text_screen("congratulation  ",(0,125,100),80,200)
				text_screen("HIGHSCORE:  "+str(highscore),(0,125,100),80,250)
			for event in pygame.event.get():
				cur=pygame.mouse.get_pos()
				if event.type == pygame.QUIT:
					run = False
				if keys[pygame.K_a] or 610>cur[0]>510 and 900>cur[1]>850:
					pygame.draw.rect(win, (200,150,0),(510,850,100,50))
					pygame.mixer.music.load("13724_alan_walker_on_my_way_marimba_remix_ringtone_2019_ringtone_mp3.mp3")
					pygame.mixer.music.play(100)
					x=200
					y=200
					v_x=3
					v_y=0
					score=1
					snk_len=1
					snk_size=[]
					game_over=False
				if keys[pygame.K_ESCAPE]:
					run=False
					game_over=False
			pygame.display.update()
			
			
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	x+=v_x
	y+=v_y
			
	
	if keys[pygame.K_LEFT]:
		v_x=0
		v_x=-5
		v_y=0
		
	if keys[pygame.K_RIGHT]:
		v_x=0
		v_x=5
		v_y=0
	if keys[pygame.K_UP]:
		v_y=0
		v_x=0
		v_y=-5
	if keys[pygame.K_DOWN]:
		v_y=0
		v_x=0
		v_y=5
	if -10<(x - randx) <10 and -10< (y - randy )<10 :
		randx=random.randint(20,700)
		randy=random.randint(20,780)
		score += 1
		
	snk_size.append(x)
	snk_size.append(y)
	win.fill((0,0,0))
	win.blit(bgmg,(0,0))
	res(0,0,720,20)
	res(0,0,20,800)
	res(705,0,20,800)
	res(0,800,720,20)
	text_screen("score: "+str((score-1)*10),(0,0,120),16,0)
	text_screen("highscore: "+highscore,(0,0,120),330,0)
	pygame.draw.circle(win, (0,225,0),(randx,randy),w)
	
	pygame.draw.rect(win, (100,100,0),(280,850,150,100))
	text_screen("UP",(0,0,200),320,870)
	pygame.draw.rect(win, (100,100,0),(280,1150,150,100))
	text_screen("DN",(0,0,200),320,1160)
	pygame.draw.rect(win, (100,100,0),(120,1000,150,100))
	text_screen("LEFT",(0,0,200),130,1015)
	pygame.draw.rect(win, (100,100,0),(440,1000,155,100))
	text_screen("RIGHT",(0,0,200),435,1015)
	pygame.draw.rect(win, (100,100,0),(110,850,100,50))
	text_screen("| |",(0,0,200),140,841)
	pygame.draw.rect(win, (100,100,0),(510,850,100,50))
	text_screen("|>",(0,0,200),540,841)
	
	cur=pygame.mouse.get_pos()
	if 430>cur[0]>280 and 950>cur[1]>850:
		pygame.draw.rect(win, (200,150,0),(280,850,150,100))
		v_y=0
		v_x=0
		v_y=-5
	if 410>cur[0]>280 and 1250>cur[1]>1150:
		pygame.draw.rect(win, (200,150,0),(280,1150,150,100))
		v_y=0
		v_x=0
		v_y=5
	if 250>cur[0]>120 and 1100>cur[1]>1000:
		pygame.draw.rect(win, (200,150,0),(120,1000,150,100))
		v_y=0
		v_x=-5
		v_y=0
	if 595>cur[0]>440and 1100>cur[1]>1000:
		pygame.draw.rect(win, (200,150,0),(440,1000,155,100))
		v_y=0
		v_x=5
		v_y=0
	if 210>cur[0]>110 and 900>cur[1]>850:
		pygame.draw.rect(win, (200,150,0),(110,850,100,50))
		pause=True
		while pause:
			text_screen("PAUSED", (0,0,0),250,300)
			pygame.display.update()
			cur=pygame.mouse.get_pos()
			if 610>cur[0]>510 and 900>cur[1]>850:
				pygame.draw.rect(win, (200,150,0),(510,850,100,50))
				pause=False
		
		
	for i in range(0,len(snk_size),2):
		pygame.draw.circle(win, (60,10,50), (snk_size[i],snk_size[i+1]),w)
	if x in snk_size[0:-2:2] :
		if y ==snk_size[snk_size.index(x)+1]:
			game_over=True
	if y in snk_size[1:-2:2] :
		if x ==snk_size[snk_size.index(y)-1]:
			game_over=True
	snk_len += 1
	if (score*10)<snk_len:
		del snk_size[0]
		del snk_size[0]
		snk_len -=1
	if x<20 or x>700or y<20 or y>780:
		game_over=True
		
		
	
	pygame.display.update()
	pygame.time.Clock().tick(150)
pygame.quit()
quit()