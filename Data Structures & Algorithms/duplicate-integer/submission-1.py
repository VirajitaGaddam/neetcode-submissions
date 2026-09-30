class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_add = set()

        for i in nums:
            if i in nums_add:
                return True
            nums_add.add(i)

        return False