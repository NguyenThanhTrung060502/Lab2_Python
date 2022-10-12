from Color import color

print("""===========================================
                 PART 1
===========================================""")

def flag():
    for i in range(3):
        print("     " + color.red + ' ' * 30 + color.end)
    for i in range(3):
        print("     " + color.white + ' ' * 30 + color.end)
    for i in range(3):
        print("     " + color.blue + ' ' * 30 + color.end)

flag()
print("""===========================================
                 PART 2
===========================================""")

array = [[0 for i in range(13)] for j in range(13)]
for i in range(1,8):
    for j in range(13):
        array[i][j] = str(array[i][j])
        if i == 2 or i == 6:
            array[i][1] = "X"
            array[i][5] = "X"
            array[i][6] = "X"
            array[i][10] = "X"
        if i == 3 or i ==5 :
            array[i][2] = "X"
            array[i][4] = "X"
            array[i][7] = "X"
            array[i][9] = "X"
        if i == 4:
            array[i][3] = "X"
            array[i][8] = "X"
        if i == 1 or i == 7:
            array[i][0] = "X"
            array[i][11] = "oo"
        if j == 6:
            array[1][j] = "1"
            array[7][j] = "1"

for i in range(1,8):
    line = ""
    for j in range(13):
        if array[i][j] == "X":
            line += "  " +  color.white 
        elif array[i][j] == "oo":
            line += "   " + color.white 
        elif array[i][j] == "1":
            line += " " + color.white 
        else:
            line += "  " + color.black 
    line += color.end
    print(line)

print("""==========================================
                 PART 3
==========================================""")

def create_array(array):
    for i in range(12):
        for j in range(12):
            if j == 0:
                array[i][j] = 11 - i
            if i == 11:
                array[i][j] = j

def fill_array(array):
    for i in range(11):
        for j in range(12):
            if 11 - i == 2*j and j != 0:
                array[i][j] = 1 
                array[i+1][j] = 1

def print_graph(array):
    for i in range(11):
        line = ""
        for j in range(12):
            if j == 0:
                array[i][j] = 11 - i
                line += "        " + color.black + color.end + color.cyan + "  " 
            if array[i][j] == 1 and j != 0:
                line +=  color.white + "  "
            elif  array[i][j] == 0:
                line += color.red + "  " 
        line += color.end
        print(line)
    print("        " + color.black + color.end + color.cyan + '0 1 2 3 4 5 6 7 8 9 10  ' + color.end)

array_2 = [[0 for i in range(12)] for j in range(12)]

create_array(array_2)
fill_array(array_2)
print_graph(array_2)

print("""==========================================
                PART 4
==========================================""")

file = open("books.csv", encoding = "windows-1251")
header = file.readline()
arr_date = []
line = file.readline()
while line != "":
    line = line.split(";")  
    arr_date.append(line[6])
    line = file.readline()
file.close()

count = 0
amount_1 = 0
amount_2 = 0
arr_year = []

lenght = len(arr_date)

for i in range(lenght):
    for j in range(2000,2023):
        j = str(j)
        if j in arr_date[i]:
            arr_year.append(j)
            count += 1

for a in arr_year:
    if int(a) <= 2016:
        amount_1 += 1
    elif int(a) > 2016:
        amount_2 += 1
print("Количество книг по состоянию до 2016 год (<=2016): " + str(amount_1) + "\n")
print("Количество книг после 2016 года (>2016): " + str(amount_2) + "\n")

arr = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    for j in range(6):
        if j == 1 or j == 3:
            arr[6][j] = 1
            arr[7][j] = 1
            arr[8][j] = 1
            arr[9][j] = 1
            arr[5][1] = 1
            arr[4][1] = 1
        if j == 0:
            arr[i][j] = (10-i)*10

def print_graph(array):
    for i in range(1,10):
        line = ""
        for j in range(5):
            if array[i][j] == 1:
                line += color.red + "  " + color.white + "    "
            if arr[i][j] == 0 and j != 0:
                line += color.red + "      "
            if j == 0:
                line +=  "       " + color.black + color.end + color.cyan + str(arr[i][j])
        line += color.end 
        print(line)

print("Диаграмма процента книг до и после 2016 года (%)")
print("\n")
print(color.black + "      " + color.cyan + "100" + color.red + "                        " + color.end)
print_graph(arr)
print(color.black + "       " + color.cyan + " 0 <=2016      >2016      " + color.end)
