n=int(input())
s=input()
colors=input()
# cur=0
# for i in range(len(s)):
#     s[i],cur=[cur,cur+len(s[i])],cur+len(s[i])
# cur=0
# count=0
# for j in s:
#     for i in range(j[0],j[-1]):
#         if i!=j[0]:
#             if colors[i-1]==colors[1]:
#                 count+=1
#                 break
# print(count)
i=j=0
prev=False
count=0
ind=0
while j<n:
    if prev==False:
        prev=True
        i+=1
        j+=1
    elif s[i]==' ':
        i+=1
        prev=False
        ind=0
    else:
        if ind==0:
            if colors[j]==colors[j-1]:
                count+=1
                ind=1
                # print(i,j,prev)
                # print(colors[j-1],colors[j])
        i+=1
        j+=1

print(count)