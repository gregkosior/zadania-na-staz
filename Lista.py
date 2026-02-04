# podana jest lista zawierajacza elementy o wartosci 1-n. Napisz funkcjie ktora sprawdzi jakich elementow brakuje
# 1-n = [1,2,3,4,5,..,10]
# np n=10
# wejscie : [2,3,7,4,9],10
# wyjscie : [1,5,6,8,10]

def znajdz_brakujace_elementy(lista, n):
    brakujace = []
    for i in range(1, n + 1):
        if i not in lista:
            brakujace.append(i)
    return brakujace
# Przykład użycia
wejscie = [2, 3, 7, 4, 9]
n = 10
wynik = znajdz_brakujace_elementy(wejscie, n)
print(wynik)  # Output: [1, 5, 6, 8, 10]

