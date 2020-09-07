import collections


# DFS solution.
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        def killAll(pid, children, killed):
            killed.append(pid)
            for child in children[pid]:
                killAll(child, children, killed)

        result = []
        children = collections.defaultdict(set)
        for i in range(len(pid)):
            children[ppid[i]].add(pid[i])
        killAll(kill, children, result)
        return result
val=Solution()
s,m=map(int,input().split())
arr1=list(map(int,input().split()))
arr=list(map(int,input().split()))
print(*val.killProcess(arr1,arr,m))
