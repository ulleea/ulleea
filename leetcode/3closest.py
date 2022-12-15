def threeSumClosest( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if max(nums)>abs(min (nums)): sum = 3*(max(nums)+target)
    else: sum=3*(abs(min (nums))+target)
    nums.sort()
    print(nums)
    n = len(nums)
    for i in range(n - 2):
        if i!=0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]-target
            if abs(s) < abs(sum):
                sum = s
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                break
    return sum+target

a=[1,1,1,1]
b=3
print(threeSumClosest(a,b))
