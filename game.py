#V0.0.1
#Pre-Alpha

#основные переменные
game = True         #состояние игры (активна, выключена)
world = [['0']]     #переменная мира (расположение объектов)

#параметры
HOTPF = 11          #высота игрового поля
WOTPF = 23          #ширина игрового поля

#создание мира
world[0] = world[0] * WOTPF
world = world * HOTPF

#игра
while game == True:

	#вывод мира
	for x1 in range(len(world)):
		tmp = ''
		for x2 in world[x1]:
			tmp = tmp + x2
		print (tmp)


	input ()