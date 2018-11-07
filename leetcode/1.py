class Solution():
    def twoSum(self, nums, target):
        n = len(nums)

        for x in range(n):
            for y in range(x+1,n):
                if nums[y] == target - nums[x]:
                    return x,y
                    break
                else:
                    continue


demo = Solution()
print(demo.twoSum([2,7,11,15],9))