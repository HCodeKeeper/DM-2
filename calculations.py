import numpy as np
matrix = [ [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 1, 0, 0],
            [1, 0, 0, 0, 0]]
print("matrix: ")
for i in range(5) :
    print(matrix[i])

#Отношение эквиваленотности

print("Отношение эквивалентности: ")

def reflection():
    reflex = True
    for i in range(len(matrix)):
        if matrix[i][i] == matrix[i-1][i-1] and matrix[i][i] == 1:
            continue
        else:
            reflex = False
        
    return reflex

def not_reflective():
    reflex = True
    for i in range(len(matrix)):
        if matrix[i][i] == matrix[i-1][i-1] and matrix[i][i] == 0:
            reflex = False
    return reflex


def symmetry():
    symm = True
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != matrix[j][i]:
                symm = False
    return symm


def equality_relation(trans, symm, reflex):
    result = True
    if trans == False or symm == False or reflex == False:
        result = False
    return result

#Частичный порядок


def antisymmetry():
    antisymm = True
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == matrix[j][i]:
                antisymm = False
    return antisymm


def partial_order(trans, antisymm, reflex):
    partorder = True
    if trans == False or antisymm == False or reflex == False:
        partorder = False
    return partorder


#Строгий порядoк



def anti_reflex():
    anti_reflex = True
    for i in range(len(matrix)):
        if matrix[i][i] != matrix[i-1][i-1] and matrix[i][i] != 0:
            anti_reflex = False
    
    return anti_reflex


def strict_order(trans, antisymm, antireflex):
    strictorder = True
    if trans == False or antisymm == False or antireflex == False:
        strictorder = False

    print(strictorder)
    return strictorder

#Возведение в степень

def _pow_util(matrix_a, matrix_b, power, calls=1):
    matrix_a = matrix_a.copy()
    matrix_b = matrix_b.copy()
    result_arr = []
    for j, _ in enumerate(matrix_a):
        row = []
        for i, _ in enumerate(matrix_b[j]):
            element = 0
            for k, _ in enumerate(matrix_b):
                element += matrix_a[j][k] * matrix_b[k][i]
            row.append(0 if element == 0 else 1)
        result_arr.append(row)
    calls += 1
    if calls >= power:
        return result_arr
    else:
        return _pow_util(result_arr, matrix_a, power, calls)

def pow_matrix(matrix, n):
    return _pow_util(matrix, matrix, n)

def subset(a, b):
    for _, elemA in enumerate(a):
        if elemA not in b:
            return False
    return True

#Замыкания
def diagonal_matrix(matrix):
    result_matrix = []
    for i,_ in enumerate(matrix):
        row = []
        for j, _ in enumerate(matrix[i]):
            row.append(1 if i == j else 0)
        result_matrix.append(row)
    return result_matrix

def closure(matrixA, matrixB):
    result_closure = []
    for i, _ in enumerate(matrixA):
        row = []
        for j, _ in enumerate(matrixA[i]):
            row.append(1 if matrixA[i][j] == 1 or matrixB[i][j] == 1 else 0)
        result_closure.append(row)
    return result_closure

def transponate_matrix(matrix):
    result_matrix = []
    for i, _ in enumerate(matrix):
        row = []
        for j, _ in enumerate(matrix[i]):
            row.append(matrix[j][i])
        result_matrix.append(row)
    return result_matrix

def reflective_closure(matrix):
    return closure(matrix, diagonal_matrix(matrix))


def symmetric_closure(matrix):
    return closure(matrix, transponate_matrix(matrix))


def transitive_closure(matrix):
    return closure(matrix, pow_matrix(matrix, len(matrix[0])))

#Транзитивность

def is_transitive(matrix):
    result_matrix = pow_matrix(matrix, 2)
    return subset(matrix, result_matrix)
