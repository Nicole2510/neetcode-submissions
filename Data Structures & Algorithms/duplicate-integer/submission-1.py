class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupl_nums = {}
        for number in nums:
            if number in dupl_nums:
                return True
            
            dupl_nums[number] = 1
        return False

        