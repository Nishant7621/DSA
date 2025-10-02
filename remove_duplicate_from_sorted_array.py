class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        start = 0
        for i in range(1, n):
            if nums[i] != nums[start]:
                start += 1
                nums[start] = nums[i]
        return start + 1


# create object of Solution
obj = Solution()
l = [1, 2, 2, 2, 3, 4, 5,4]

k = obj.removeDuplicates(l)  
print("Unique length:", k)
print("Modified list:", l[:k]) 