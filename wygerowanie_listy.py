# nalezy wygenerowac liste liczb od 2 do 5.5 ze skokiem co 0.5 , dane wynikowe musza byc w typie decimal

from decimal import Decimal
def wygeneruj_liste_decimal(start, end, step):
    lista = []
    current = Decimal(start)
    end = Decimal(end)
    step = Decimal(step)
    while current <= end:
        lista.append(current)
        current += step
    return lista
# Przykład użycia
wynik = wygeneruj_liste_decimal(2, 5.5, 0.5)
print(wynik)  # Output: [Decimal('2'), Decimal('2.5'), Decimal('3'), Decimal('3.5'), Decimal('4'), Decimal('4.5'), Decimal('5'), Decimal('5.5')]