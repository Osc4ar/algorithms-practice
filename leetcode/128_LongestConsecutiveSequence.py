class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSequence = 0
        set_nums = set(nums)

        for n in set_nums:
            if (n - 1) not in set_nums:
                sequence = 1
                current_num = n

                while (current_num + 1) in set_nums:
                    current_num += 1
                    sequence += 1

                if sequence > longestSequence:
                    longestSequence = sequence

        return longestSequence
 