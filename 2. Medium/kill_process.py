class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
#         mapping = collections.defaultdict(list)
#         for i in range(len(ppid)):
#             mapping[ppid[i]].append(pid[i])

#         queue = [kill]
#         result = []
#         while queue:
#             kill = queue.pop(0)
#             result.append(kill)
#             if kill in mapping:
#                 queue += mapping[kill]

#         return result

        mapping = {}
        for i in range(len(ppid)):
            if ppid[i] in mapping:
                mapping[ppid[i]].append(pid[i])
            else:
                mapping[ppid[i]] = [pid[i]]

        ans = []
        q = deque()
        q.append(kill)
        while q:
            k = q.popleft()
            ans.append(k)
            if k in mapping:
                q += mapping[k]

        return ans
