class Solution:
    def findMin(self,nums):
        # maximum = max(nums)
        # position = nums.index(maximum)
        # if position == len(nums)-1: return nums[0]
        # else: return nums[position+1]
        begin, end = 0, len(nums)-1
        while begin<end:
            mid = begin + (end-begin)//2
            if nums[mid] > nums[end]: begin = mid+1
            else: end = mid
        return nums[begin]
sol = Solution()
print(sol.findMin([3,4,5,1,2]))
print(sol.findMin([4,5,6,7,0,1,2]))
print(sol.findMin([11,13,15,17]))