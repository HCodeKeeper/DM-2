from calculations import *

_reflection = reflection()
_symmetry = symmetry()
_transitivity = is_transitive(matrix)
_equality_relation = equality_relation(_transitivity, _symmetry, _reflection)
_antisymm = antisymmetry()
_partial_order = partial_order(_transitivity, _antisymm, _reflection)
_antireflex = anti_reflex()

print("Рефликсивность: ", _reflection)
print("Симметричность: ", _symmetry)
print("Транзитивность: ", _transitivity)
print("Эквивалентность: ", _equality_relation)
print()

print("Антисимметричность: ", _antisymm)

print("Проверка на частичную порядочность: ", _partial_order)

print("Антирефликсивность: ", _antireflex)

print("Проверка на строгую порядочность: ", strict_order(_transitivity, _antisymm, _antireflex))

print("Антитранзитивность: ", not _transitivity)

print("Заданая матрица в степени 2: ", pow_matrix(matrix, 2))
print("Заданая матрица в степени 3: ", pow_matrix(matrix, 3))
