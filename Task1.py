# Задача 1. Создайте программу для игры в "Крестики-нолики".

size = 3
matrix = [["-" for j in range(size)] for i in range(size)]

def print_field():
    for i in range(size):
        print(' '.join(matrix[i]))
def pl_inp_x():
    while True:
        try:
            numX = int(input('Введите значение строчки: '))
            if numX<1 or numX>size:
                print('Число не в размерах поля')
                continue
        except ValueError:
            print('Это не число')
        else:
            return numX
def pl_inp_y():
    while True:
        try:
            numY = int(input('Введите значение столбика: '))
            if numY<1 or numY>size:
                print('Число не в размерах поля')
                continue
        except ValueError:
            print('Это не число')
        else:
            return numY
def hod_0(x,y):
    global matrix
    matrix[x-1][y-1] = '0'
def hod_X(x,y):
    global matrix
    matrix[x-1][y-1] = 'X'
def res():
    count = 0
    global matrix
    for j in range(size):
        count = 0
        for i in range(size-1):
            if matrix[i][j] == matrix[i+1][j] and matrix[i][j] != '-':
                count += 1
        if count == 2:
            return True
    for i in range(size):
        if matrix[i].count(matrix[i][j]) == len(matrix[i]) and matrix[i][j] != '-':
            return True
    count = 0
    for i in range(size-1):
        if matrix[i][i] == matrix[i+1][i+1] and matrix[i][i] != '-':
            count += 1
    if count == 2:
        return True
    count = 0
    for i in range(size-1):
        if matrix[i][-1-i] == matrix[i+1][-2-i] and matrix[i][-1-i] != '-':
            count += 1
    if count == 2:
        return True   
def game():
    global matrix
    print('Добро пожаловать в крестики-нолики)')
    print_field()
    player = 'X'
    for r in range(size*size):
        if player == 'X':
            print('Ходят крестики')
            x = pl_inp_x()
            y = pl_inp_y()
            while matrix[x-1][y-1] != '-':
                print('Эта ячейка занята')
                x = pl_inp_x()
                y = pl_inp_y()
            hod_X(x,y)
            if res() == True:
                print('Поздравляем! Крестики выиграли')
                print_field()
                break
            player = '0'
        else:
            print('Ходят нолики')
            x = pl_inp_x()
            y = pl_inp_y()
            while matrix[x-1][y-1] != '-':
                print('Эта ячейка занята')
                x = pl_inp_x()
                y = pl_inp_y()
            hod_0(x,y)
            if res() == True:
                print('Поздравляем! Нолики выиграли')
                print_field()
                break
            player = 'X'
        print_field()
    if res() == None:
        print('Увы, НИЧЬЯ!')
        
game()
        

