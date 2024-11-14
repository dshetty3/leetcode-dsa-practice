class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """


        result = []

        words = text.split()

        for i in range(2, len(words)):
            if words[i - 2] == first and words[i - 1] == second:
                result.append(words[i])
        return result
        