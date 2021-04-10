from collections import deque
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        store = []
        num = 0

        if not s:
            return num
        for i in range(size):
            if s[i] not in store:
                store.append(s[i])
                #if len(store) > 2 and store.count(store[-2])>1:
                #    store.remove(store[-2])
                #if len(store) > 2 and store[0]==store[1]:
                #    store.popleft()
            elif s[i] in store:
                num = max(len(store),num)
                store.append(s[i])
                idx = store.index(s[i]) + 1
                for i in range(idx):
                    store.pop(0)
        num = max(num, len(store))
        return num
