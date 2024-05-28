dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Your code goes here
# create a list of every vowel that appears in the strs
vowels = 'aeiou'
chars = []
for key in dict1:
    for word in dict1[key]:
        for char in word:
            if char in vowels:
                chars.append(char)
                
list_of_vowels = [char for key in dict1 
                        for word in dict1[key]
                        for char in word if char in vowels]

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']