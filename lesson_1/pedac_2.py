"""
Sort Strings by most adjacent consonants

input: list of strs
output: new sorted list where strs are sorted based on highest n of adjacent consonants a str contains

Explicit rules:
    - if two strs contain same highest n of adj consonants, retain original order in relation to each other
    - adj consonants are valid also if the str is separated by a space but consonants are next to each other ignoring the space

Implicit rules:
    - strs can be multiple words
    - Strings may contain single or multiple words.
    - Strings may not be empty.
    - Strings may have no adjacent consonants.
    - Strings should be sorted in descending order.
    - Case is not relevant.
    - Single consonants don't affect sort order

Questions:
    - Can strings be empty?
        - no empty strs it seems from test cases
    - Is it possible for a str to have no adj consonants?
        - yes
    - case?
        - all lowercase
    - Sort in ascending or descending order?
        - descending

DS:
    - just lists i think...
    - jk maybe hash map

Algo:
    - Iterate through given list
        - count highest n of adj consonants for each str
        - save each str as key in dict and highest n of adj consonant as value
    - Make new list based on values of dict

"""

def count_max_adjacent_consonants(str):
    new_str = str.replace(" ", "")
    max_consonants = 0
    adj_cons_str = ""
    vowels = ["a", "e", "i", "o", "u"]

    for c in new_str:
        if c not in vowels:
            adj_cons_str += c
            if len(adj_cons_str) > max_consonants:
                if len(adj_cons_str) > 1:
                    max_consonants = len(adj_cons_str)
        elif len(adj_cons_str) > max_consonants:
            if len(adj_cons_str) > 1:
                max_consonants = len(adj_cons_str)
            adj_cons_str = ""
    
    return max_consonants

def sort_by_consonant_count(strings):
    strings.sort(key=count_max_adjacent_consonants, reverse=True)
    return strings

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
