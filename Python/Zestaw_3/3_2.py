""" Podpunkt 1

L = [3, 5, 4] ; L = L.sort()

Komentarz: Metoda sort() sortuje liste in-place, ale nie zwraca zadnej
wartosci. Robi to natomiast metoda sorted(), ktora zwraca nowo utworzona,
posortowana liste.
"""
L = [3, 5, 4] ; L.sort()
# lub
L = [3, 5, 4] ; L = sorted(L)

""" Podpunkt 2

x, y = 1, 2, 3

Komentarz: Liczba zmiennych musi byc rowna liczbie wartosci do przypisania.
"""
x, y, z = 1, 2, 3
# lub
x, y = 1, 2

""" Podpunkt 3

X = 1, 2, 3 ; X[1] = 4

Komentarz: Krotki sa niemodyfikowalne, w przeciwienstwie do np. list.
"""
X = [1, 2, 3] ; X[1] = 4

""" Podpunkt 4

X = [1, 2, 3] ; X[3] = 4

Komentarz: Indeks 3 jest poza zasiegiem listy. Iteracja list zaczyna sie od 
indeksu zerowego.
"""
X = [1, 2, 3] ; X[2] = 4
# lub (w zaleznosci od intencji)
X = [1, 2, 3] ; X.append(4)

""" Podpunkt 5

X = "abc" ; X.append("d")

Komentarz: Stringi nie obsluguja metody append(). Konkatenacja lancuchow 
znakow odbywa sie poprzez operacje dodawania.
"""
X = "abc" ; X += "d"

""" Podpunkt 6

L = list(map(pow, range(8)))

Komentarz: Funkcja pow() przyjmuje dwa argumenty - podstawe i wykladnik. 
"""
L = list(map(pow, range(8), range(8)))
