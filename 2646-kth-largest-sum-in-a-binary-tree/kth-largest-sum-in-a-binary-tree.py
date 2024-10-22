# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        q = deque([root])
        minHeap = []

        while q:
            level_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            heapq.heappush(minHeap, level_sum)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return -1 if len(minHeap) < k else minHeap[0]        