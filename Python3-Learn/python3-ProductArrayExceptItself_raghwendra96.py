
# Author - Raghwendra Singh
# python3 - Product of array elements except itslef and for more light on concept see the example below
# GITHUB - https://github.com/raghwendra96

# Input : 1 2 3 4
# Output : [24, 12, 8, 6]

def getProduct(arr):
    if arr is None or len(arr) == 0:
        return arr

    n = len(arr)
    res = [0]*n
    product = 1

    for i in range(n):
        product *= arr[i]
        res[i] = product
    
    product = 1

    for i in range(n-1,0,-1):
        res[i] = res[i-1]*product
        product *=arr[i]
    
    res[0] = product

    return res

inp = [int(x) for x in input().split(' ')]

print(getProduct(inp))

#sample input output

# py Product_Array_Except_Itself.py
# 1 2 3 4
# [24, 12, 8, 6]


