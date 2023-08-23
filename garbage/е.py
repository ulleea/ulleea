ind1=ind2=ind3=ind4=0
stck=[-1]
ex=1
s=input()
se={'(',')', '[',']', '{','}', '<','>'}
# print('[' in se)
for i in s:
    # print(i in se)
    # print(i, type(i),stck)
    if  (i in se)== False:
        # print('NO')
        # print('=-=-')
        ex=0
        break
    if i=='(':
        stck.append('(')
        ind1+=1
    elif i=='[':
        stck.append('[')
        ind2+=1
    elif i=='{':
        stck.append('{')
        ind3+=1
    elif i=='<':
        stck.append('<')
        ind4+=1

    elif i==')':
        x=stck.pop()
        ind1-=1
        if x!='(' or x==-1:
            # print('NO')
            ex=0
            break
    elif i==']':
        x=stck.pop()
        ind2-=1
        if x!='[' or x==-1:
            # print('NO')
            ex=0
            break
    elif i=='}':
        x=stck.pop()
        ind3-=1
        if x!='{' or x==-1:
            # print('NO')
            ex=0
            break
    elif i=='>':
        x=stck.pop()
        ind4-=1
        if x!='<' or x==-1:
            # print('NO')
            ex=0
            break
    if ind1<0 or ind2<0 or ind3<0 or ind4<0 :
        # print('NO')
        ex=0
        break

if ind1==0 and ind2==0 and ind3==0 and ind4==0 and ex:
    print('YES')
else:
    print('NO')