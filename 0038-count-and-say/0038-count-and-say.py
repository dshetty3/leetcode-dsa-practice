class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """


        if n == 1:
            return "1"
        
        seq = "1"
        for _ in range(n - 1):
            stack = []
            count = 1
            new_seq = []

            for i in range(1, len(seq)):
                if seq[i] == seq[i - 1]:
                    count += 1
                else:
                    stack.append((count, seq[i - 1]))
                    count = 1
            stack.append((count, seq[-1]))

            while stack:
                c, num = stack.pop(0)
                new_seq.append(str(c) + num )

            seq = "".join(new_seq)
            
        return seq
        