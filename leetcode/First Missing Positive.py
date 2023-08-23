nums=[7,8,9,11,12]
nums=set(nums)
i=1
while True:
    if i in nums:
        i+=1
    else:
        break
print(i)