#V0.0.2
#Pre-Alpha

#import keyboard

class TheWorld ():
	'''класс мира'''

	HOTPF = 10           #высота игрового поля
	WOTPF = 30          #ширина игрового поля
	world = [[" "]]
	frame = [['┌','─','┐'],
		   	 ['│',' ','│'],
			 ['└','─','┘']]
	skin_of_tne_world = "░"

	def __init__(self):
		'''создание игрового пространства'''
		self.world[0] = self.skin_of_tne_world
		tmp = self.world #переменная игрового мира
		tmp[0] = tmp[0] * self.WOTPF #растягривание по ширине
		tmp = tmp * self.HOTPF #растягивание по высоте
		self.world = tmp #сохранение в классе

	def print_world(self):
		'''вывод мира'''
		print (self.frame[0][0]+self.frame[0][1]*self.WOTPF+self.frame[0][2])
		for x1 in range (len (self.world)):
			tmp = ''
			for x2 in self.world[x1]:
				tmp = tmp + str(x2)
			print (self.frame[1][0] + tmp + self.frame[1][2])
		print (self.frame[2][0]+self.frame[2][1]*self.WOTPF+self.frame[2][2])


	def TEW (self):
		'''технический вывод мира'''
		print (" ")
		for x in self.world:
			print (x)
		print (" ")

class Player (TheWorld):
	"""класс отвечающий за главного персонажа (игрока)"""

	x = 8              #положение игрока по оси X      
	y = 3              #положение игрока по оси Y
	skin = '☺'         #скин игрока
	speed_go = [0,0]

	def __init__(self):
		pass

	def gamer(self):
		'''создние игрока'''
		c = list(theworld.world[self.y])
		c[self.x] = self.skin
		theworld.world[self.y] = c

	def hide_the_player (self):
		'''удаление игрока с поля'''
		c = list(theworld.world[self.y])
		c[self.x] = theworld.skin_of_tne_world
		theworld.world[self.y] = c

	def go (self):
		'''метод двигающий игрока'''
		old_xy = [self.x, self.y]		
		if old_xy[0] == 0 or old_xy[1] == 0 or old_xy[0] == theworld.WOTPF - 1 or old_xy[1] == theworld.HOTPF - 1:
			print ("Вы упёрлисьв стенку. Ваш персонваж умер.") 			
			self.hide_the_player ()
			self.x = round(theworld.WOTPF / 2)
			self.y = round(theworld.HOTPF / 2)
			self.gamer ()
		else:
			self.hide_the_player ()
			print (self.speed_go)
			self.x = self.x + self.speed_go[0]
			self.y = self.y + self.speed_go[1]
			self.gamer ()
			self.speed_go[0] = 0
			self.speed_go[1] = 0

		 
theworld = TheWorld ()          #создание объекта Мир
player = Player ()              #создание объекта Игрок

player.gamer ()				    #создание игрока

time = 0

for time in range (100 + time):             #основной игроввой цикл

	#!!! theworld.TEW ()             #техническтий вывод мира
	theworld.print_world ()     #вывод игрового пространства Мира

	input_plaer = input (":")

	#консольные комнды
	if input_plaer == "/stop_game" or input_plaer == "/s":
		break
	elif input_plaer == "/time":
		print (time)
	#движение
	elif input_plaer == "вв":
		player.speed_go[1] = -1 
	elif input_plaer == "вп":
		player.speed_go[0] = 1
	elif input_plaer == "вн":
		player.speed_go[1] = 1
	elif input_plaer == "вл":
		player.speed_go[0] = -1
	#неверный ввод
	else:
		print ("Команды " + input_plaer + " не существует.")

	player.go ()
		