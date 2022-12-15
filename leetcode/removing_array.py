def removeDuplicates( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cur = None
    i=0
    count=0
    n=len(nums)
    while count<len(nums):
        if nums[i] != cur:
            cur = nums[i]
            i+=1
        else:
            n-=1
            nums.pop(i)
            nums.append(0)
            # for j in range(i + 1, len(nums)):
            #     nums[j], nums[j - 1] = nums[j - 1], nums[j]
        count+=1
    return n

nums=[1,1,2]
k=removeDuplicates(nums)
print(k,nums)
print(nums[:k])
