lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

# return a list that conatins only the dicts where all nums are even

def is_even(dic):
    # access value
    for lst in dic.values():
        for n in lst:
            if n % 2 != 0:
                return False
    return True
    # iterate through list and determine if all nums are even
    # if all even
    # return dic

res = [dic for dic in lst if is_even(dic)]

print(res)