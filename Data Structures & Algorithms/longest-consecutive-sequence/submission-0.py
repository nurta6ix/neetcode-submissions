class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max = 0
        for i in nums:
            if i - 1 not in nums:
                counter = 0
                buf = i
                while buf in nums:
                    counter += 1
                    buf += 1

                if counter > max: max = counter

        return max