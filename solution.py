from functools import lru_cache

@lru_cache(maxsize=128)
def _task1_cached(search_tuple, data):
    search = dict(search_tuple)
    lines = data.splitlines()
    headers = lines[0].split(',')
    if 'value' not in headers:
        raise ValueError("Missing value column")
    key_order = [h for h in headers if h != 'value']
    if set(search.keys()) != set(key_order):
        raise Exception("Key mismatch")
    value_idx = headers.index('value')
    key_indices = [headers.index(k) for k in key_order]
    for line in lines[1:]:
        parts = line.split(',')
        if all(str(parts[i]) == str(search[k]) for i, k in zip(key_indices, key_order)):
            return parts[value_idx]
    return '-1'

def task1(search: dict, data: str) -> str:
    return _task1_cached(tuple(sorted(search.items())), data)

@lru_cache(maxsize=128)
def _task2_cached(search_list_tuple, data):
    search_list = [dict(t) for t in search_list_tuple]
    lines = data.splitlines()
    headers = lines[0].split(',')
    if 'value' not in headers:
        raise ValueError("Missing value column")
    key_order = [h for h in headers if h != 'value']
    for search in search_list:
        if set(search.keys()) != set(key_order):
            raise Exception("Key mismatch")
    value_idx = headers.index('value')
    key_indices = [headers.index(k) for k in key_order]
    search_set = {tuple(str(search[k]) for k in key_order): None for search in search_list}  # type: dict[tuple[str, ...], int | None]
    total_weighted = 0
    total_weight = 0
    for line in lines[1:]:
        parts = line.split(',')
        key = tuple(parts[i] for i in key_indices)
        if key in search_set and search_set[key] is None:
            value = int(parts[value_idx])
            weight = 20 if value % 2 == 0 else 10
            total_weighted += value * weight
            total_weight += weight
            search_set[key] = value
            if all(v is not None for v in search_set.values()):
                break
    if total_weight == 0:
        return "0.0"
    return f"{total_weighted / total_weight:.1f}"

def task2(search_list: list, data: str) -> str:
    search_list_tuple = tuple(tuple(sorted(d.items())) for d in search_list)
    return _task2_cached(search_list_tuple, data)
