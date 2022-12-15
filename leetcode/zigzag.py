s="abc"
n=len(s)
# print(n)
numRows=2
l=0
for i in range(numRows):
    string=s[i]
    sp1=' '*(numRows-2-l)
    sp2=' '*(l-1)
    j=i+(numRows*2-2)
    while j<n:
        if l==0 or l==numRows-1:
            string+=sp1+sp2+s[j]
        else:
            string+=sp1+s[j-l-i]+sp2+s[j]
        j+=(numRows*2-2)
    if (l!=0) and (l!=numRows-1) and (j-l-i<n):
        print(j,l,i,s[j-l-i])
        string+=s[j-l-i]
    l+=1
    print(string.strip())


# n=len(s)
# l=0
# string=''
# for i in range(numRows):
#     string+=s[i]
#     j=i+(numRows*2-2)
#     while j<n:
#         if l==0 or l==numRows-1:
#             string+=s[j]
#         else:
#             string+=s[j-l-i]+s[j]
#         j+=(numRows*2-2)
#     l+=1
# print( string)