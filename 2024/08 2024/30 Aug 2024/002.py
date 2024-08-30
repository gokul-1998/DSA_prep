nums = [2,7,11,15]
target = 9
# Output: [0,1]

def two_sum(nums,target):
    seen = {}
    for i, num in enumerate(nums):
        remaining = target - num
        if remaining in seen:
            return [seen[remaining], i]
        seen[num] = i
    return None

print(two_sum(nums,target))