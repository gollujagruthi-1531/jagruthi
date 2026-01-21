nums = [23, 87, 45, 12, 99, 4, 56, 71]

big = nums[0]
small = nums[0]

for n in nums:
    if n > big:
        big = n
    if n < small:
        small = n

print("Biggest number:", big)
print("Smallest number:", small)
