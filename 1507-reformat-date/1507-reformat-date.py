class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """

        s = date.split()

        monthDict = {'Jan': '01', 'Feb': '02', 
              'Mar': '03', 'Apr': '04', 
              'May': '05', 'Jun': '06', 
              'Jul': '07', 'Aug': '08', 
              'Sep': '09', 'Oct': '10', 
              'Nov': '11', 'Dec': '12'}

        day = s[0][:-2]
        month = monthDict[s[1]]
        year = s[2]

        if int(day) < 10:
            day = '0' + day

        res = year + '-' + month + '-' + day
        return res
                