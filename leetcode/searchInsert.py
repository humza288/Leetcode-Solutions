def searchInsert(nums, target) -> int:
    try:
        return nums.index(target)
    except:
        for i in nums:
            if i > target:
                return nums.index(i)
        return len(nums) + 1

print(searchInsert([1, 3, 5, 6], 7))
