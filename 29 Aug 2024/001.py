#  SOLUTION 1

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set=set(nums)
        missing_number=None
        for i in range(len((nums))+1):
            if i not in nums_set:
                return i

        
        
#  SOLUTION 2
# explanation : https://chatgpt.com/share/c4a09299-9d6e-4e5c-af40-32b0336f2a34

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
