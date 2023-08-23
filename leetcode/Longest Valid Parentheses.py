s=')()())'
max_length = 0
stck=[-1] # initialize with a start index
for i in range(len(s)):
    # print('-----')
    # print(i,s[i],stck)
    if s[i] == '(':
        stck.append(i)
    else:
        stck.pop()
        if not stck: # if popped -1, add a new start index
            # print('not',stck )
            stck.append(i)
        else:
            # print(i,'max')
            max_length=max(max_length, i-stck[-1]) # update the length of the valid substring
    # print(stck)
print(max_length)

