class Solution(object):
    
    def nextPermutation(self, nums):
        index = self.getIndex(nums)

        if (len(nums) == 2):
            return self.swap(nums, 0, 1)
        
        if (len(nums) == 1):
            return nums

        if index == -1:
            return self.reverse(0, nums)

        otherIndex = self.changIndex(nums, index)
        nums = self.swap(nums, otherIndex, index)
        nums = self.reverse(index + 1, nums)
        return nums

    def getIndex(self, nums):
        
        i = len(nums) - 1

        while(i > 0):
            if nums[i - 1] >= nums[i]:
                i -= 1
            else:
                return i - 1

        return -1
    
    def changIndex(self, nums, i):
        
        j = len(nums) - 1

        while (j >= i):
            if (nums[j] > nums[i]):
                return j
            else:
                j -= 1
    
        
    def swap(self, A, i, j):
        A[i], A[j] = (A[j], A[i])
        
        return A

    def reverse(self, i, nums):
        start = i
        end = len(nums) - 1

        while (start < end):
            nums = self.swap(nums, start, end)
            start += 1
            end -= 1

        return nums

sln = Solution()

print(sln.nextPermutation([5, 1, 1]))