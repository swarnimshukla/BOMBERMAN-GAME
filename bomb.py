from bomberman import *
import os
import signal,copy,sys,time
class Bomb:
	def __init__ (self):
		self._id=5
		self._count=0
		self._time =0
		self._flag=0
		self._ti=3
		self._placebomb=0
	def placement(self,p1,p2,a):
		if(self._count<1):	
			a[p1][p2]=self._id
			self._count+=1
			self._time=time.time()
			self._flag = 0
			self._placebomb=1

	def	check(self):

		if(time.time()-self._time>3):
			if self._count:
				return 4
		self._ti=3 - int(time.time()-self._time)
		return self._ti	
		# sys.exit(0)
	def findenemy(self,e1,e2,enemy_arr):
		for i in enemy_arr:
			if(i._x==e1 and i._y==e2):
				enemy_arr.remove(i)	
	
	def explode(self,a,p1,p2,enemy_arr,score):
		self._placebomb=0
		if(a[p1+1][p2]==2):
			a[p1+1][p2]=0
			score+=20
			print('Your score is',score)
		if(a[p1+1][p2]==3):
			a[p1+1][p2]=0
			score+=100
			self.findenemy(p1+1,p2,enemy_arr)
			print('Your score is',score)
		if(a[p1+1][p2]==4):
			os.system('tput reset')
			print('Game over')
			print('Your score is',score)
			sys.exit(0)	
		if(a[p1-1][p2]==2):
			a[p1-1][p2]=0
			score+=20
			print('Your score is',score)
		if(a[p1-1][p2]==3):
			a[p1-1][p2]=0
			score+=100
			self.findenemy(p1-1,p2,enemy_arr)
			print('Your score is',score)
		if(a[p1-1][p2]==4):
			os.system('tput reset')
			print('Game over')
			print('Your score is',score)
			sys.exit(0)	
		if(a[p1][p2+1]==2):
			a[p1][p2+1]=0
			score = score + 20
			print('Your score is',score)
		if(a[p1][p2+1]==3):
			a[p1][p2+1]=0
			score+=100
			self.findenemy(p1,p2+1,enemy_arr)
			print('Your score is',score)
		if(a[p1][p2+1]==4):
			os.system('tput reset')
			print('Game over')
			print('Your score is',score)
			sys.exit(0)	
		if(a[p1][p2-1]==2):
			a[p1][p2-1]=0
			score+=20
			print('Your score is',score)
		if(a[p1][p2-1]==3):
			a[p1][p2-1]=0
			score+=100
			self.findenemy(p1,p2-1,enemy_arr)
			print('Your score is',score)
		if(a[p1][p2-1]==4):
			os.system('tput reset')
			print('Game over')
			print('Your score is',score)
			sys.exit(0)	
		if(a[p1][p2]==4):	
			os.system('tput reset')
			print('Game over')
			print('Your score is',score)
			sys.exit(0)	
			
		a[p1+1][p2]=6
		a[p1-1][p2]=6
		a[p1][p2+1]=6
		a[p1][p2-1]=6
		a[p1][p2]=6	
		return score
	