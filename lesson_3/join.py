def join_or(lst, conj1=', ', conj2='or'):
    # insert conjunctions before the last element
    # return string of sequence of elements + conjunctions + last element
    res = []
    if not lst:
        return ""
    elif len(lst) == 1:
        return str(lst[0])
    elif len(lst) == 2:
        return f"{lst[0]} {conj2} {lst[1]}"
    else:
        res = conj1.join(str(num) for num in lst[0:-1])
        return f"{res}{conj1}{conj2} {lst[-1]}"

print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"

"""
input: list of ints, up to 2 strings
output: string of list elements joined by comma or second arg and third arg before the last element

explicit rules:
    - return empty string is empty list

implicit rules:
    - if only 2 items, conj1 isn't used
    - default for conj2 is or

DS:
    - just lists and strings I think?

Algo:
    - initial thought: push elements onto new list
    - push conj2 before pushing last element
    - return conj1.join(res)
"""

