class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            ans = []
            j = target - nums[i]
            if (j in nums) and nums.index(j) != i:
                ans.append(i)
                ans.append(nums.index(j))
            else:
                continue
            ans.sort()
            return ans;