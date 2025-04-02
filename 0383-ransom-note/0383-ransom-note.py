class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # if Counter(ransomNote) in Counter(magazine):
        #     return False
        # else:
        #     return True


        counter = Counter(magazine)

        # for c in magazine:
        #     if c in counter:
        #         counter[c] += 1 #if already there then increment the counter
        #     else:
        #         counter[c] = 1 #else new value: start from 1

        for c in ransomNote:
            if c not in counter:
                return False
            elif counter[c] == 1:
                counter.pop(c)
            else:
                counter[c] -= 1
        return True

        