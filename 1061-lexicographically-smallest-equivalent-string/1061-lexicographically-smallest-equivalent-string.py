class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """

        g = defaultdict(list)

        for a, b in zip(s1, s2):
            g[a].append(b)
            g[b].append(a)

        def dfs(ch, visit):
            visit.add(ch)
            min_ch = ch
            for nei in g[ch]:
                if nei not in visit:
                    candidate = dfs(nei, visit)
                    min_ch = min(min_ch, candidate)
            return min_ch

        res = []
        for c in baseStr:
            visit = set()
            res.append(dfs(c, visit))

        return ''.join(res)        