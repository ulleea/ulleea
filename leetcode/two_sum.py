def func():
    num=[1,2,3,4,5,6]
    target=9
    n=len(num)
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if num[i]+num[j]==target:
    #             return [i,j]
    for i, n in enumerate(num):
        print(i,n)
