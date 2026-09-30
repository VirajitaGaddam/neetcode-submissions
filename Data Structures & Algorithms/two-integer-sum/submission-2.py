class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        
        nums_map = {}
        
        for i, n in enumerate(nums):
            nums_map[n] = i
        
        for i in range(0, len(nums)):
            check_num  = target - nums[i]
            if check_num in nums_map and nums_map[check_num] != i:
                return [i, nums_map[check_num]]