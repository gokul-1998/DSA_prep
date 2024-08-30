nums = [1,2,3,4,5,6,7]
k = 3
# Output: [5,6,7,1,2,3,4]
def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums
print(rotate(nums, k))


def rotate2(nums, k):
    # this wont work if k > len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums
nums = [1,2,3,4,5,6,7]
k = 3
print(rotate2(nums, k))

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        nums[:] = nums[-k:] + nums[:-k]