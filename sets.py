# deklaracja zbioru
first_set = {1, 1, 1}

print(first_set)  # wynikiem będzie -> {1}

# konwersja listy na zbiór
moja_lista = [1, 5, 3, 8, 6, 6, 1]
first_set = {1, 2, 6, 7}
second_set = set(moja_lista)

print(second_set)

# siła operacji na zbiorach
# suma zbioru
print(first_set | second_set)
print(first_set.union(second_set))

# część wspólna
print(first_set & second_set)
print(first_set.intersection(second_set))

# różnica
print(first_set - second_set)
print(second_set - first_set)
print(first_set.difference(second_set))

# coś co występuje jednym lub drugim zbiorze, ale nie w obu jednocześnie
print(first_set ^ second_set)
print(first_set.symmetric_difference(second_set))

# podstawowe metody
