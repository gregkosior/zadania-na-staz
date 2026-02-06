from solution import task1, task2

def test_task1():
    data = 'side,currency,value\nIN,PLN,1\nIN,EUR,2\nOUT,ANY,3'
    assert task1({'side': 'IN', 'currency': 'PLN'}, data) == '1'
    assert task1({'side': 'IN', 'currency': 'GBP'}, data) == '-1'
    print('task1 tests passed')

def test_task2():
    data = 'side,currency,value\nIN,PLN,1\nIN,EUR,2\nOUT,ANY,3'
    search_list = [
        {'side': 'IN', 'currency': 'PLN'},
        {'side': 'OUT', 'currency': 'EUR'},
    ]
    result = task2(search_list, data)
    assert result == '1.0', f"Expected 1.0, got {result}"
    print('task2 tests passed')

if __name__ == "__main__":
    test_task1()
    test_task2()
