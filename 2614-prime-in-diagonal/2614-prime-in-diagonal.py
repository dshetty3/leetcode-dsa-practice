class Solution(object):
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        prime = []

        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if i == j or i + j == len(nums) - 1:
                    if is_prime(nums[i][j]):
                        prime.append(nums[i][j])
        return max(prime) if prime else 0
        
                