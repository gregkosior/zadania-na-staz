from solution import task2

search_list = [
    {'a': 862984, 'b': 29105, 'c': 605280, 'd': 678194, 'e': 302120},
    {'a': 20226, 'b': 781899, 'c': 186952, 'd': 506894, 'e': 325696}
]

filename = "find_match_average_v2.dat"

with open(filename, encoding="utf-8") as f:
    data = f.read()

print(task2(search_list, data))
