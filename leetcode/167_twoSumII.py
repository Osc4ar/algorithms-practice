class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        validated_nums = set()

        for index, num in enumerate(numbers[:-1]):
            if num in validated_nums:
                continue

            complement_index = index + 1
            current_sum = num + numbers[complement_index]

            while current_sum <= target and complement_index < len(numbers):
                current_sum = num + numbers[complement_index]
                if current_sum == target:
                   return [index + 1, complement_index + 1]

                complement_index += 1

            validated_nums.add(num)

        return [-1, -1]