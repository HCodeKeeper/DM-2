import numpy as np
matrix = np.array([ [1, 0, 1, 0, 1],
                    [1, 0, 1, 1, 0],
                    [0, 1, 0, 0, 1],
                    [1, 0, 1, 0, 0],
                    [1, 0, 0, 0, 0]])
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

def pow_matrix(matrix, n):
    matrix = matrix.copy()
    new_matrix = matrix.copy()
    sum = 0
    if n <= 1:
        return matrix
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                for l in range(len(matrix)):
                    sum += matrix[i][l] * matrix[l][j]
                
                new_matrix[i][j] = 1 if sum > 0 else 0
                sum = 0
        return pow_matrix(new_matrix, n-1)

def subset(a, b):
    for _, elemA in enumerate(a):
        if elemA not in b:
            return False
    return True

#Транзитивность

def is_transitive(matrix, elems=5):
    result_matrix = pow_matrix(matrix, elems)
    return subset(matrix, result_matrix)
