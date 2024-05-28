lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

def increment_values(dict):
    return {key: value + 1 for key, value in dict.items()}

res = [increment_values(value) for value in lst]