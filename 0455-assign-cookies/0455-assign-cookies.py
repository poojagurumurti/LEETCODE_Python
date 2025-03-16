class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n = len(g)    #greedy children
        m = len(s)    # greedy cookies
        l=r=0
        g.sort()
        s.sort()

        while l<m and r<n:
            if s[l] >= g[r]:
                r +=1
            l +=1
        return r
        