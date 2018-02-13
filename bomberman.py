from random import randint
import signal,copy,sys,time
import os
class Person:
	def __init__(self,x,y,id):
		self._x=x
		self._y=y
		self._id=id
		self._flag=0

	def moveright(self,a):
		if(a[self._x][self._y+1]==0 and a[self._x][self._y+1]!=1):
			a[self._x][self._y+1]=self._id
			if(a[self._x][self._y]==0 or a[self._x][self._y] == self._id):
				a[self._x][self._y]=0
			self._y=self._y+1
			return 1
		elif(a[self._x][self._y+1]==4 and self._id==3):
			return 2
		return 0				

	def moveleft(self,a):
		if(a[self._x][self._y-1]==0 and a[self._x][self._y-1]!=1):
			a[self._x][self._y-1]=self._id
			if(a[self._x][self._y]==0 or a[self._x][self._y] == self._id):
				a[self._x][self._y]=0		
			self._y=self._y-1
			return 1
		elif(a[self._x][self._y-1]==4 and self._id==3):
			return 2
		return 0				
	
	def movedown(self,a):
		if(a[self._x+1][self._y]==0 and a[self._x+1][self._y]!=1):
			a[self._x+1][self._y]=self._id
			if(a[self._x][self._y]==0 or a[self._x][self._y] == self._id):
				a[self._x][self._y]=0		
			self._x=self._x+1	
			return 1
		elif(a[self._x+1][self._y]==4 and self._id==3):
			return 2
		return 0				

	def moveup(self,a):
		if(a[self._x-1][self._y]==0 and a[self._x-1][self._y]!=1):
			a[self._x-1][self._y]=self._id
			if(a[self._x][self._y]==0 or a[self._x][self._y] == self._id):
				a[self._x][self._y]=0		
			self._x=self._x-1		
			return 1
		if(a[self._x-1][self._y]==4 and self._id==3):
			return 2	
		return 0				
			
class Bomberman(Person):
	def __init__(self):
		Person.__init__(self,1,1,4)

class Enemy(Person):
	def __init__ (self,a):
		self._x=randint(5,17)
		self._y=randint(5,17)
		self._id=3
		self._time=time.time()
		self._flag=0
		self._mo=[self.moveup,self.movedown,self.moveleft,self.moveright]
		if(a[self._x][self._y]==0 ):
			a[self._x][self._y]=self._id

	def enemymovement(self,a,enemy_time):
			if(time.time()-self._time>enemy_time):
				posi=randint(0,3)
				for i in range(0,4):
					if(self._mo[(i+posi)%4](a)==1):
						break
					if(self._mo[(i+posi)%4](a)==2):
						self._flag=1
													
				self._time=time.time()					
				