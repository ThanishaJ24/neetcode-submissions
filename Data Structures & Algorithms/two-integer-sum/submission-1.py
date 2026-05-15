class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i]+nums[j]==target and i!=j:
        #             return [i,j]
        d={}
        for i in range(len(nums)):
            c=target-nums[i]
            if c in d:
                return [d[c],i] 
            d[nums[i]]=i           


        