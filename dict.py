# definicja słownika
slownik = {}

# dodanie lub zmiana elementów słownika
slownik["id"] = 1
slownik["nazwa"] = "Ala"

print(slownik)

# pobranie elementu słownika
value = slownik.get("id")
print(value)

# loop

for i in slownik:
    print(i)

for i, j in slownik.items():
    print(i, j)
    # gdzie i to klucz słownika, a j to wartość przypisana do klucza

print(slownik.values())
print(slownik.keys())
