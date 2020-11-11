# Describe the differences between in-place and out-of-place algorithms

# in-place algorithm
x = []
n = [1, 2, 3]
def tripple_in_place(nums):
    for index in range(len(nums)):
        # nums[index] = nums[index] * 3
        nums[index] *= 3

print(n)
x = tripple_in_place(n)
print(n)

print(x)