class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = title.split()
        res = []

        for word in words:
            if len(word) > 2:
                res.append(word[0].upper() + word[1:].lower())
            else:
                res.append(word.lower())
        return ' '.join(res)


        