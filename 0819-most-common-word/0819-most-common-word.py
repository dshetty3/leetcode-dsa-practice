class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        bannedSet = set(banned)
        words = paragraph.replace('!', '').replace("'", ' ').replace('?', '').replace('.', '').replace(',', ' ').replace(';', '').lower().split()



        for word in words:
            if word in bannedSet:
                words.remove(word)

        words1 = Counter(words)
        max_count = max(words1.values())

        for word in words1:
            if words1[word] == max_count:
                return word


        
        