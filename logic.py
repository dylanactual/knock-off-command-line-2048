import random


def start_game():
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    mat [3][random.randint(0,3)] = 2 ** random.randint(1,2)
    return mat

def display(mat):
    for i in range(4):
        print(mat[i])
        
#returns a tuple indicating which index to put new number in and the new number respectively
#input free is a binary list of indices that are free for new number    
def new_numbers(free):
    index = random.randint(0, (len(free) - 1))
    number = 2 ** random.randint(1, 2)
    return (free[index], number)

#transposes square matrix one-quarter turn anticlockwise
#input a matrix and optionally number of rotations. Default one turn
#outputs the transposed matrix
def transpose(matrix):
    temp = []
    for i in range(4):
        vec = []
        for j in range(4):
            vec.append(matrix[j][i])
        temp.insert(0, vec)
    return temp


#inputs a matrix returns a matrix affected by gravity
#ie numbers "above" 0's "fall" down
def gravity(matrix):
    changed = True
    while (changed):
        changed = False
        for i in range(3):
            for j in range(4):
                if matrix[i][j] != 0 and matrix[(i+1)][j] == 0:
                    matrix[(i+1)][j] = matrix[i][j]
                    matrix[i][j] = 0
                    changed = True
    return matrix

#inputs a matrix, outputs the matrix with likes combined
def combine(matrix):
    for i in range(3, 0, -1):
        for j in range(4):
            if matrix[i][j] == matrix[(i-1)][j]:
                matrix[i][j] += matrix[(i-1)][j]
                matrix[(i-1)][j] = 0
    return matrix

#copies a matrix onto another one
def copy(matrix):
    mat2 = []
    for i in range(4):
        mat2.append([0] * 4)
        for j in range(4):
            mat2[i][j] = matrix[i][j]
    return mat2

#strings together combine and gravity for one iteration of a movement
def action(matrix):
    gravity(matrix)
    combine(matrix)
    gravity(matrix)
    return matrix

#returns the status of the game: 0 still in play, 1 game over, 2 win
#takes two matrices: mat1 before action and mat2 after action
def state(mat1, mat2):
    if mat1 == mat2: return 1
    for i in range(4):
        for j in range(4):
            if mat2[i][j] == 2048: return 2
    return 0

#down action, s on the keyboard
def s(matrix):
    matrix2 = copy(matrix)
    action(matrix2)
    free = []
    for i in range(4):
        if matrix2[0][i] == 0: free.append(i)
    numbers = new_numbers(free)
    matrix2[0][numbers[0]] = numbers[1]
    st = state(matrix, matrix2)

    return matrix2, st

#left action
def a(matrix):
    matrix2 = copy(matrix)
    matrix2 = transpose(matrix2)
    
    action(matrix2)
    free = []
    for i in range(4):
        if matrix2[0][i] == 0: free.append(i)
    numbers = new_numbers(free)
    matrix2[0][numbers[0]] = numbers[1]
    matrix2 = transpose(matrix2)
    matrix2 = transpose(matrix2)
    matrix2 = transpose(matrix2)

    st = state(matrix, matrix2)
    return matrix2, st
    
#up action
def w(matrix):
    matrix2 = copy(matrix)
    matrix2 = transpose(matrix2)
    matrix2 = transpose(matrix2)
    action(matrix2)
    free = []
    for i in range(4):
        if matrix2[0][i] == 0: free.append(i)
    numbers = new_numbers(free)
    matrix2[0][numbers[0]] = numbers[1]
    matrix2 = transpose(matrix2)
    matrix2 = transpose(matrix2)
    st = state(matrix, matrix2)
    return matrix2, st

def d(matrix):
    matrix2 = copy(matrix)
    matrix2 = transpose(matrix2)
    matrix2 = transpose(matrix2)
    matrix2 = transpose(matrix2)
    action(matrix2)
    free = []
    for i in range(4):
        if matrix2[0][i] == 0: free.append(i)
    numbers = new_numbers(free)
    matrix2[0][numbers[0]] = numbers[1]
    matrix2 = transpose(matrix2)
    st = state(matrix, matrix2)
    return matrix2, st

    

