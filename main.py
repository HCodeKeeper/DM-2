from calculations import *
from pprint import pprint

_symmetry = symmetry()
_transitivity = is_transitive(matrix)
_reflective = reflection()
_non_reflective = not_reflective()
_equality_relation = equality_relation(_transitivity, _symmetry, _reflective)
_antisymm = antisymmetry()
_partial_order = partial_order(_transitivity, _antisymm, _reflective)
_antireflex = anti_reflex()

print("Рефликсивна: ", _reflective)
print("Антирефликсивна: ", _non_reflective)
print("Симметричность: ", _symmetry)
print("Транзитивность: ", _transitivity)
print("Эквивалентность: ", _equality_relation)
print()

print("Антисимметричность: ", _antisymm)

print("Проверка на частичный порядок: ", _partial_order)

print("Антирефликсивность: ", _antireflex)

print("Проверка на строгий порядок: ", strict_order(_transitivity, _antisymm, _antireflex))

print("Антитранзитивность: ", not _transitivity) ##

print("Заданая матрица в степени 2: ")
pprint(pow_matrix(matrix, 2))

print("Заданая матрица в степени 3: ")
pprint(pow_matrix(matrix, 3))

print("Рефлексивное замыкание")
pprint(reflective_closure(matrix))

print("Симметричное замыкание")
pprint(symmetric_closure(matrix))

print("Транзитивное замыкание")
pprint(transitive_closure(matrix))
