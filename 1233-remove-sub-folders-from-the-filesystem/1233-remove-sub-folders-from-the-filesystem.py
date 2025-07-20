class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """

        res = []
        folders = set(folder)

        for f in folder:
            res.append(f)
            for i in range(len(f)):
                if f[i] == '/' and f[:i] in folders:
                    res.pop()
                    break
        return res



        