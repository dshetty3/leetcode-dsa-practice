class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """

        s_queue = []
        t_queue = []


        for i in range(len(start)):
            if start[i] != '_':
                s_queue.append((start[i], i))
            if target[i] != '_':
                t_queue.append((target[i], i))
        
        if len(s_queue) != len(t_queue):
            return False

        while len(s_queue) != 0:
            s_char, s_index = s_queue.pop(0)
            t_char, t_index = t_queue.pop(0)

            if (
                s_char != t_char or
                (s_char == 'L' and s_index < t_index) or
                (s_char == 'R' and s_index > t_index)
            ):
                return False

        return True
        