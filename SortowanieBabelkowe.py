import random

maxx = 100

i=0
max_liczba = random.randint(0,maxx)

lista = []

while i <= max_liczba:
  lista.append(random.randint(0, max_liczba*10))
  i += 1

print("Lista przed sortowaniem: ", "\n", lista)

print("\n")

def przestawienie(x):
  i = 0
  while i < len(x)-1:
    if x[i] > x[i+1]:
      pamiec1 = x[i]
      x[i] = x[i+1]
      x[i+1] = pamiec1
      i += 1
    else:
      i += 1

i = 0
while i < len(lista):
  przestawienie(lista)
  i += 1
  
print("Lista po sortowaniu: ", "\n", lista)
