n=10
left,right=1,n
last=None
ans=guess(right)
if ans==0:
    print(right)
elif guess(left)==0:
    print(left)
else:
    gues= (right+left) // 2
    ans=guess(gues)
    last=gues
    while ans!=0:
        if ans==1:
            left=gues
            gues= (right + left) // 2
        elif ans==-1:
            right=gues
            gues = (right + left) // 2
        if gues==last:
            gues+=1
        ans = guess(gues)
        last=gues
    print(gues)