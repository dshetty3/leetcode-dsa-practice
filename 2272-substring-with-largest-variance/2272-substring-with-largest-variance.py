class Solution(object):
    def largestVariance(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = set(s)
        res = 0
        

        for a in counter:
            for b in counter:
                if a == b: continue

                count_a = count_b = 0
                has_b = False

                for ch in s:
                    if ch != a and ch != b:
                        continue
                
                    if ch == a:
                        count_a += 1
                    elif ch == b:
                        count_b += 1
                        has_b = True
                    if has_b:
                        res = max(res, count_a - count_b)
                    else:
                        res = max(res, count_a - 1)
                    
                    if count_b > count_a:
                        count_a = 0
                        count_b = 0
                        has_b = False
                
                count_a = count_b = 0
                has_b = False

                for ch in reversed(s):
                    if ch != a and ch != b:
                        continue
                
                    if ch == a:
                        count_a += 1
                    elif ch == b:
                        count_b += 1
                        has_b = True
                    if has_b:
                        res = max(res, count_a - count_b)
                    else:
                        res = max(res, count_a - 1)
                    
                    if count_b > count_a:
                        count_a = 0
                        count_b = 0
                        has_b = False

        return res
        