#V0.0.1.2
#Pre-Alpha

class TheWorld ():
	'''класс мира'''

	HOTPF = 5           #высота игрового поля
	WOTPF = 15          #ширина игрового поля
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

class Player ():
	"""класс отвечающий за главного персонажа (игрока)"""

	x = 8              #положение игрока по оси X      
	y = 3              #положение игрока по оси Y
	skin = '☺'         #скин игрока

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
		
	def go (self, go_in):
		'''метод двигающий игрока'''
		old_xy = [self.x, self.y]		
		if old_xy[0] == 0 or old_xy[1] == 0 or old_xy[0] == theworld.WOTPF or old_xy[1] == theworld.HOTPF:
			print ("Вы упёрлисьв стенку. Ваш персонваж умер.") 
			self.x = round(theworld.WOTPF / 2)
			self.y = round(theworld.HOTPF / 2)
			self.hide_the_player  ()
		elif go_in == 0: 
			self.hide_the_player  ()
			self.y = old_xy[1] - 1
			self.gamer ()
		elif go_in == 1:
			self.hide_the_player  ()
			self.x = old_xy[0] + 1
			self.gamer ()
		elif go_in == 2:
			self.hide_the_player  ()
			self.y = old_xy[1] + 1
			self.gamer ()
		elif go_in == 3:
			self.hide_the_player  ()
			self.x = old_xy[0] - 1
			self.gamer ()
		else:
			print ("ОШИБКА МЕТОДА \"Player.go\". Неверное значение аргумента go_in.")
		
		 
theworld = TheWorld ()          #создание объекта Мир
player = Player ()              #создание объекта Игрок

player.gamer ()				    #создание игрока

game = True                     #состояние игры (активна, выключена)

while game == True:             #основной игроввой цикл

	#!!! theworld.TEW ()             #техническтий вывод мира
	theworld.print_world ()     #вывод игрового пространства Мира

	input_plaer = input (":")

	#консольные комнды
	if input_plaer == "/stop_game" or input_plaer == "/s":
		game = False

	#движение
	elif input_plaer == "вверх" or "вв":
		player.go (0)
	elif input_plaer == "вправо" or "вп":
		player.go (1)
	elif input_plaer == "вниз" or "вн":
		player.go (2)
	elif input_plaer == "влево" or "вл":
		player.go (3)

	#неверный ввод
	else:
		print ("Команды " + input_plaer + " не существует.")


		