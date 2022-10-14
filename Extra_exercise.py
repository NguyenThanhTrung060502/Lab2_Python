import os
from time import sleep
from Color import color

def fill_arr(array):
	for i in range(1,6):
		for j in range(16):
			if j == 1:
				array[i][j] = "t"
				array[1][0] = "t"
				array[1][2] = "t"
			if j == 3 or j == 5:
				array[i][j] = "r" 
				array[3][5] = "0"
				array[1][4] = "r" 
				array[3][4] = "r"
			if j == 6 or j == 8:
				array[i][j] = "u"
				array[5][7] = "u"
			if j == 9 or j == 11:
				array[i][j] = "n"
				array[3][10] = "n"
				array[2][10] = "N"
				array[4][10] = "L"
				array[2][11] = "M"
				array[4][11] = "M"
			if j == 12 or j == 14:
				array[i][j] = "g" 
				array[1][13] = "g" 
				array[5][13] = "g"
				array[4][13] = "g"
				array[3][14] = "0" 
				array[4][13] = "G"

def print_image(array):
	for i in range(0,6):
		line = ""
		new_line = ""
		for j in range(16):
			if array[i][j] == "t":
				line += color.red + "  "
			elif array[i][j] == "r":
				line += color.cyan + "  "
			elif array[i][j] == "u":
				line += color.magenta + "  "
			elif array[i][j] == "n":
				line += color.white + "  "
			elif array[i][j] == "M":
				line += " " + color.white + "  "
			elif array[i][j] == "N":
				line += color.white + " " + color.black 
			elif array[i][j] == "L":
				line += color.black + " " + color.white
			elif array[i][j] == "g":
				line += color.yellow + "  " + color.end
			elif array[i][j] == "G":
				line += " " + color.yellow + " "
			else:
				line += color.black + "  "
		line += color.end
		print(line)
array = [["0" for i in range(16)] for j in range(16)]
fill_arr(array)

count = 5
while count != 0:
    os.system('cls')
    sleep(1)
    print_image(array)
    count -= 1
	