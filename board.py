from __future__ import print_function
from random import randint
class Bricks:
	def __init__(self,a):
		for i in range(75):					
			self._x=randint(1,17)
			self._y=randint(1,17)
			if(a[self._x][self._y]==0 and self._x>5 and self._y>5):
				a[self._x][self._y]=2
			if(self._x==1 and self._y==1):
				a[self._x][self._y]=0		
		a[1][1]=4			

class Board:
	def __init__(self,a):
		for i in range(19):
			if(i==0 or i==18):
				for j in range(19):
					a[i][j]=1
			else:
				if(i %2==1):
						a[i][0]=1
						a[i][18]=1
				else:
					for j in range(19):
						if(j%2==0):
							a[i][j]=1	
	def	printboard(self,a):
		for i in range(38):
			if(i==0 or i==1 or i==37 or i==36):
				for j in range(19):
					print('\x1b[5;32;43m'+"XXXX"+'\x1b[0m',end='')
				print(end='\n')		
				
			else:
				if((i // 2)%2==1):
					for k in range(19):
						if(k==0):
							print('\x1b[5;32;43m'+"XXXX"+'\x1b[0m',end='')
						elif(k==18):
							print('\x1b[5;32;43m'+"XXXX"+'\x1b[0m',end='')
							print(end='\n')	
						else:
							if(a[i//2][k]==0):
								print('    ',end='')
							elif(a[i//2][k]==2):
								print('\x1b[1;33;46m'+"////"+'\x1b[0m',end='')
							elif(a[i//2][k]==3):
								print('\x1b[1;33;41m'+"EEEE"+'\x1b[0m',end='')
							elif(a[i//2][k]==4):
								print('\x1b[1;33;44m'+"BBBB"+'\x1b[0m',end='')
							elif(a[i//2][k]==5):
								print('\x1b[1;36;40m'+"OOOO"+'\x1b[0m',end='')
							elif(a[i//2][k]==6):
								print('\x1b[0;31;40m'+"eeee"+'\x1b[0m',end='')
							elif(a[i//2][k]==7):
								print("2222"+'\x1b[0m',end='')
							elif(a[i//2][k]==8):
								print("1111"+'\x1b[0m',end='')
							elif(a[i//2][k]==9):
								print("0000"+'\x1b[0m',end='')
								
				else:		 	
					for k in range(19):
						if(k%2==0 and k!=18):
							print('\x1b[5;32;43m'+"XXXX"+'\x1b[0m',end='')
						elif(k==18):
							print('\x1b[5;32;43m'+"XXXX"+'\x1b[0m',end='')
							print(end='\n')	
						else:
							if(a[i//2][k]==0):
								print('    ',end='')
							elif(a[i//2][k]==2):
								print('\x1b[1;33;46m'+"////"+'\x1b[0m',end='')	
							elif(a[i//2][k]==3):
								print('\x1b[1;33;41m'+"EEEE"+'\x1b[0m',end='')
							elif(a[i//2][k]==4):
								print('\x1b[1;33;44m'+"BBBB"+'\x1b[0m',end='')
							elif(a[i//2][k]==5):
								print('\x1b[1;36;40m'+"OOOO"+'\x1b[0m',end='')	
							elif(a[i//2][k]==6):		
								print('\x1b[0;31;40m'+"eeee"+'\x1b[0m',end='')
							elif(a[i//2][k]==7):
								print("2222"+'\x1b[0m',end='')
							elif(a[i//2][k]==8):
								print("1111"+'\x1b[0m',end='')
							elif(a[i//2][k]==9):
								print("0000"+'\x1b[0m',end='')
								
				
													
	 						
					

