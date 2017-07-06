ass Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map_nums = {}
        for index,x in enumerate(nums):
            map_nums[x] = index
        
        y = 0
        for a in nums:
            b = target - a
            x = map_nums.get(b)
            if x and x != y:
                return y,x
            y += 1
        return []
