# przyjmuje 2 stringi: "79-900" i "80-155" zwraca liste kodow miedzy nimi

def generuj_kody_pocztowe(kod_start, kod_koniec):
    kody = []
    # Podziel kody na czesc przed i po myślniku
    start_prefix, start_suffix = kod_start.split('-')
    end_prefix, end_suffix = kod_koniec.split('-')
    # Zamien na liczby całkowite
    start_prefix = int(start_prefix)
    start_suffix = int(start_suffix)
    end_prefix = int(end_prefix)
    end_suffix = int(end_suffix)
    # Generuj kody pocztowe
    for prefix in range(start_prefix, end_prefix + 1):
        suffix_start = start_suffix if prefix == start_prefix else 0
        suffix_end = end_suffix if prefix == end_prefix else 999
        for suffix in range(suffix_start, suffix_end + 1):
            kod = f"{prefix:02d}-{suffix:03d}"
            kody.append(kod)
    return kody

# Przykład użycia
kody = generuj_kody_pocztowe("79-900", "80-155")
for kod in kody:
    print(kod)

        
        
        
        



