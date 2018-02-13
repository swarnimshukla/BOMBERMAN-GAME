from board import *
from getchunix import *
from bomberman import *
from timeout import *
from time import time
from bomb import *	
import os
import signal,copy,sys,time
getch = GetchUnix()


bo_pos1 = 0
bo_pos2 = 0
enemy_arr=[]
score=0
prechart = time.time()-1
def game(level, bomberman_time, enemy_time, ene_nu):
	print('LEVEL ',level)
	time.sleep(1)
	a=[[0 for x in range(19)] for y in range(19)]
	pos = Bomberman()
	br=Bricks(a)
	b=Board(a)
	bo=Bomb()
	b.printboard(a)
	prechart = time.time()-1
	global score
	for i in range(ene_nu):
		e=Enemy(a)
		enemy_arr.append(e)
	bo_pos1 = 0
	bo_pos2 = 0
	Newscore= 0
	while 1:
		@timeout(0.2)
		def loop():
			global prechart, bo_pos1, bo_pos2,score
			c=getch()
			if(c=='q'):
				print('Your Score is ',score)
				print('Game over!!!!!')
				sys.exit(0)
			if (time.time() - prechart < bomberman_time):
				return		
			elif(c=='a'):
				prechart = time.time()
				pos.moveleft(a)
				print('Your Score is ',score)
			elif(c=='d'):
				prechart = time.time()
				pos.moveright(a)
				print('Your Score is ',score)
			elif(c=='w'):
				prechart = time.time()
				pos.moveup(a)
				print('Your Score is ',score)
			elif(c=='s'):
				prechart = time.time()
				pos.movedown(a)	
				print('Your Score is ',score)
			elif(c=='b'):
				flag=0
				for k in range(19):
					for l in range(19):
						if(a[k][l]==4):
							bo_pos1=k
							bo_pos2=l
							flag=1
							break
					if flag==1:
						break
				bo.placement(bo_pos1,bo_pos2,a)
			b.printboard(a)

			flag=0
			for k in range(19):
				for l in range(19):
					if(a[k][l]==5):
						bo_pos1=k
						bo_pos2=l
						flag=1
						break
				if flag==1:
					break
			one = bo.check()
			if(one==2):
				a[bo_pos1][bo_pos2]=7
				b.printboard(a)
			if(one==1):
				a[bo_pos1][bo_pos2]=8
				b.printboard(a)
			
			if(one == 4):
				score = bo.explode(a,bo_pos1,bo_pos2,enemy_arr,score)
				b.printboard(a)
				bo._count=0
				bo._flag=1

			elif(bo._flag==1):
				a[bo_pos1+1][bo_pos2],a[bo_pos1-1][bo_pos2],a[bo_pos1][bo_pos2+1],a[bo_pos1][bo_pos2-1],a[bo_pos1][bo_pos2]=0,0,0,0,0
				b.printboard(a)
				bo._flag=0			
			
			os.system('tput reset')
			for i in enemy_arr:
				i.enemymovement(a, enemy_time)
				if(i._flag==1):
					i._flag=0
					b.printboard(a)
					print('Game over')
					print('Enemy killed you')
					print('Your score is',score)
					sys.exit(0)	
				
			b.printboard(a)
			return
		
		try:
			loop()
		except TimeoutError:
			flag=0
			for k in range(19):
				for l in range(19):
					if(a[k][l]==5):
						bo_pos1=k
						bo_pos2=l
						flag=1
						break
				if flag==1:
					break
			one = bo.check()
			if(one==2):
				a[bo_pos1][bo_pos2]=7
				b.printboard(a)
			if(one==1):
				a[bo_pos1][bo_pos2]=8
				b.printboard(a)
			if(one == 4):
				score=bo.explode(a,bo_pos1,bo_pos2,enemy_arr,score)
				b.printboard(a)
				bo._count=0
				bo._flag=1

			elif(bo._flag==1):
				a[bo_pos1+1][bo_pos2],a[bo_pos1-1][bo_pos2],a[bo_pos1][bo_pos2+1],a[bo_pos1][bo_pos2-1],a[bo_pos1][bo_pos2]=0,0,0,0,0
				b.printboard(a)
				bo._flag=0			
			
			os.system('tput reset')
			for i in enemy_arr:
				i.enemymovement(a, enemy_time)
				if(i._flag==1):
					i._flag=0
					b.printboard(a)
					os.system('tput reset')
					print('Game over')
					print('Enemy killed you')
					print('Your score is',score)
					sys.exit(0)	
				
			b.printboard(a)
		if(enemy_arr.__len__()==0):
			break


game(1, 0.3,200,2)
os.system('tput reset')
if(enemy_arr.__len__()==0):
	game(2,0.4,0.6,8)
	os.system('tput reset')
	if(enemy_arr.__len__()==0):
		game(3,0.5,0.4,12)
