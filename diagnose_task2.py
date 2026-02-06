search_list = [
    {'a': 862984, 'b': 29105, 'c': 605280, 'd': 678194, 'e': 302120},
    {'a': 20226, 'b': 781899, 'c': 186952, 'd': 506894, 'e': 325696}
]

filename = "find_match_average_v2.dat"

header = None
found = []

with open(filename, encoding='utf-8') as f:
    header = f.readline().strip().split(',')
    value_idx = header.index('value')
    key_order = [h for h in header if h != 'value']
    key_indices = [header.index(k) for k in key_order]
    search_set = {tuple(str(search[k]) for k in key_order): None for search in search_list}
    for line in f:
        parts = line.strip().split(',')
        key = tuple(parts[i] for i in key_indices)
        if key in search_set and search_set[key] is None:
            value = parts[value_idx]
            found.append((key, value))
            search_set[key] = value
            if all(v is not None for v in search_set.values()):
                break

print("Nagłówek:", header)
print("Szukane klucze:", key_order)
print("Znalezione rekordy:")
for k, v in found:
    print(f"Klucz: {k}, value: {v}")
if not found:
    print("Nie znaleziono żadnych dopasowań.")
