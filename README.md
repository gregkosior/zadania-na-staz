# Zadania rekrutacyjne

W tym repozytorium znajdują się rozwiązania trzech zadań rekrutacyjnych w Pythonie.

## 1. Generator kodów pocztowych

Plik: `Generator_kodow_pocztowych.py`

Funkcja generuje listę kodów pocztowych pomiędzy dwoma podanymi kodami w formacie "XX-YYY" (np. "79-900" do "80-155").

**Przykład użycia:**
```python
def generuj_kody_pocztowe(kod_start, kod_koniec):
    # ...implementacja...

kody = generuj_kody_pocztowe("79-900", "80-155")
for kod in kody:
    print(kod)
```

## 2. Znajdowanie brakujących elementów w liście

Plik: `Lista.py`

Funkcja sprawdza, jakich elementów brakuje w liście liczb od 1 do n.

**Przykład użycia:**
```python
def znajdz_brakujace_elementy(lista, n):
    # ...implementacja...

wejscie = [2, 3, 7, 4, 9]
n = 10
wynik = znajdz_brakujace_elementy(wejscie, n)
print(wynik)  # Output: [1, 5, 6, 8, 10]
```

## 3. Generowanie listy typu decimal ze skokiem

Plik: `wygerowanie_listy.py`

Funkcja generuje listę liczb od 2 do 5.5 ze skokiem co 0.5, przy czym wyniki są typu `Decimal`.

**Przykład użycia:**
```python
from decimal import Decimal

def wygeneruj_liste_decimal(start, end, step):
    # ...implementacja...

wynik = wygeneruj_liste_decimal(2, 5.5, 0.5)
print(wynik)  # Output: [Decimal('2'), Decimal('2.5'), ..., Decimal('5.5')]
```

---

Każdy plik zawiera przykład użycia funkcji. Wystarczy uruchomić wybrany plik w Pythonie, aby zobaczyć wynik działania.
