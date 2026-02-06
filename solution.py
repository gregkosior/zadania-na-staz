from typing import Dict,Tuple,Optional
_cache: Optional[Dict[Tuple[str, ...], str]] = None
_key_order: Optional[list[str]] = None

_cache = None
_key_order = None

def _build_cache(data: str):
    global _cache , _key_order
    
    lines = data.strip() .split('\n')
    headers = lines[0].split(',')
    
    if 'value' not in headers:
        raise ValueError("Missing value column ")
    
    _key_order = [h for h in headers if h != 'value']
    value_index = headers.index('value')
    cache = {}
    for line in lines[1:]:
        parts = line.split(',')
        key = tuple(parts[headers.index(k)] for k in _key_order)
    
        cache[key] = parts[value_index]

    _cache = cache
    
def task1(search: dict , data : str) -> str:
    global _cache, _key_order
    if _cache is None or _key_order is None:
        _build_cache(data)
    if _key_order is None or _cache is None:
        raise RuntimeError("Cache or key order not initialized.")
    if set(search.keys()) != set(_key_order):
        raise ValueError("Key mismatch")
    key = tuple(search[k] for k in _key_order)
    return _cache.get(key, "-1")

def task2(search_list: list , data : str) -> str:
   
    global _cache, _key_order
    if _cache is None or _key_order is None:
        _build_cache(data)
    if _key_order is None or _cache is None:
        raise RuntimeError("Cache or key order not initialized.")
    total_weighted = 0
    total_weight = 0
    for search in search_list:
        if set(search.keys()) != set(_key_order):
            raise Exception("Key mismatch")
        key = tuple(search[k] for k in _key_order)
        value = _cache.get(key)
        if value is None:
            continue
        value = int(value)
        weight = 20 if value % 2 == 0 else 10
        total_weighted += value * weight
        total_weight += weight
    if total_weight == 0:
        return "0.0"
    return f"{total_weighted / total_weight:.1f}"

     
if __name__ == "__main__":
    data = 'side,currency,value\nIN,PLN,1\nIN,EUR,2\nOUT,ANY,3'
    # Test task1
    print("task1 test 1:", task1({'side': 'IN', 'currency': 'PLN'}, data))  # Expected: '1'
    print("task1 test 2:", task1({'side': 'IN', 'currency': 'GBP'}, data))  # Expected: '-1'
    # Test task2
    search_list = [
        {'side': 'IN', 'currency': 'PLN'},
        {'side': 'OUT', 'currency': 'EUR'},
    ]
    print("task2 test:", task2(search_list, data))  # Expected: '1.0'


        
        
        
    