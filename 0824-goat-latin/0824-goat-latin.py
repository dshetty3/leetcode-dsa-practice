class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """

        words = sentence.split()
        res = []
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for index, word in enumerate(words):
            if word[0][0].lower() not in vowels:
                res.append(word[1:]+ word[0][0] + 'ma' + 'a' * (index + 1))
            elif word[0][0].lower() in vowels:
                res.append(word + 'ma' + 'a' * (index + 1))
        return ' '.join(res)


        