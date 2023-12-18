# testowanie działania array i iteracji po nditer
# nie nadaj się chyba do drukowania macierzy ale może nadawać się 
# do obliczania czy zachodzi cykl itp
import numpy as np


macierz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


for liczba in np.nditer(macierz):
    print(liczba)
