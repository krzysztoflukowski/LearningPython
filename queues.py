# kolejki

from collections import deque

moja_kolejka = deque([])
moja_kolejka.append(1)
moja_kolejka.append(3)
moja_kolejka.append(5)
moja_kolejka.append(5)
moja_kolejka.append(5)

print(moja_kolejka)
print(moja_kolejka.rotate(2))

moja_kolejka.appendleft(10)

print(moja_kolejka)

print(moja_kolejka.count(5))

moja_kolejka.extend([1, 2, 3])
