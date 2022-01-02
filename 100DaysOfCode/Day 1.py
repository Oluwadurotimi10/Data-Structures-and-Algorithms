"""
Sorting numbers according to the sum of their digits
"""
#solution 1
def summ(num):
    summ = 0
    while num != 0:
       summ += num%10 
       num //= 10
    return summ

def sort_digits(nums):
    num_map = {}
    for i in nums:
        num_map[i] = summ(i)
    return sorted((list(num_map.values())))

#solution2    
def sort_digitss( nums):
    num_map = {}
    for i in nums:
        num_map[i] = sum(list(map(int, str(i).strip())))
    
    return sorted(list(num_map.values()))

nums = [12,67,1111,78]
print(sort_digits(nums))