class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        m=height[0]
        left=[m]
        for i in range(1,n):
            if height[i]>m:
                m=height[i]
            if m>height[i]:
                left.append(m)
            else:
                left.append(height[i])
        m=height[-1]
        right=[m]
        for i in range(n-2,-1,-1):
            if height[i]>m:
                m=height[i]
            if m>height[i]:
                right.append(m)
            else:
                right.append(height[i])
        right=right[::-1]
        ans=[0]*n
        for i in range(n):
            ans[i]=min(left[i],right[i])-height[i]
        return sum(ans) 