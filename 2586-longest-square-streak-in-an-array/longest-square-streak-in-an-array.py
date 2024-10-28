class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)  # Convert nums to a set for quick lookup
        max_length = 0  # Track the longest square streak found

        for n in nums:
            current_length = 0
            current = n

        # Build the streak by checking if the next square exists
            while current in num_set:
                current_length += 1
                current = current ** 2  # Move to the next square

        # Update the maximum length
            max_length = max(max_length, current_length)

    # If no streak longer than 1 was found, return -1; otherwise, return max_length
        return max_length if max_length > 1 else -1
    

    