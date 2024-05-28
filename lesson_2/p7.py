lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

def mult_three(nums):
    return [num for num in nums if num % 3 == 0]

res = [mult_three(sublist) for sublist in lst]

print(res)