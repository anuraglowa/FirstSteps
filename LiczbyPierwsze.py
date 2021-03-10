def iledzielnikow(liczba):
  licznik = 0
  i = 1
  while i <= liczba:
    if liczba % i == 0:
      licznik += 1
      i += 1
    else:
      i +=1
    if licznik == 3:
      break
  return licznik

liczod = 1
liczdo = 1000

while liczod <= liczdo:
  if iledzielnikow(liczod) == 2:
    print(liczod)
    liczod += 1  
  else:
    liczod += 1
