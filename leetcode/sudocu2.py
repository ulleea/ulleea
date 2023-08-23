def solver(vert,gor,quad,pot,acc,filled,temp,board,deep):
    # print(deep)
    # for i in range(1,10):
    #     if len(acc[i])!=0:
    #         print(i,len(acc[i]),':',acc[i])
    # for k in filled.keys():
    #     i = k // 9
    #     j = k % 9
    #     board[i][j] = str(filled[k])
    # for i in range(9):
    #     print(board[i])
    # t1 = [quad, gor, vert, pot, acc, temp, filled]
    for j in range(1,10):
        if acc[j]:
            i=j
            break
        elif j==9:
            return [1,filled]
    if acc[i]:
        x=acc[i].pop()
        while pot[x]:
            a = pot[x].pop()
            filled[x] = a
            gr = x // 9
            vr = x % 9
            vert[vr] -= {a}
            gor[gr] -= {a}
            quad[(gr // 3) * 3 + vr // 3] -= {a}
            temp.add(x)

            for i in range(n): #пересекаем
                for j in range(n):
                    if i*9+j not in temp:
                        l = pot[i * 9 + j]
                        pot[i * 9 + j] = quad[(i // 3) * 3 + j // 3] & vert[j] & gor[i]
                        if len(pot[i * 9 + j])==0 and len(l) != len(pot[i * 9 + j]):
                            # print('wrong', i * 9 + j)
                            # print('======')
                            # print('deep',deep)
                            # print('2ss', x, pot[x], a)
                            # print('quad', quad)
                            # print('vert', vert)
                            # print('gor', gor)
                            # print('temp', temp)
                            # print('acc', acc[1], acc[2], acc[3], acc[4], acc[5], acc[6])
                            # print('filled', filled)
                            pot[i * 9 + j]=l
                            vert[vr] |= {a}
                            gor[gr] |= {a}
                            quad[(gr // 3) * 3 + vr // 3] |= {a}
                            temp.remove(x)

                            return [0]  # wrong!!

            acc = {i: set() for i in range(10)}
            for k in range(n ** 2): #делаем acc
                if k not in temp:
                    acc[len(pot[k])].add(k)
                else:
                    acc[0].add(k)
            # print('======')
            # print('2ss', x,pot[x],a)
            # print('quad',quad)
            # print('vert',vert)
            # print('gor',gor)
            # print('temp', temp)
            # print('acc', acc[1], acc[2], acc[3], acc[4], acc[5], acc[6])
            # print('filled', filled)
            # print('---')

            b=solver(vert,gor,quad,pot,acc,filled,temp,board,deep+1)
            if not b[0]:
                # quad, gor, vert, pot, acc, temp, filled = t1[0], t1[1], t1[2], t1[3], t1[4], t1[5], t1[6]
                vert[vr] |= {a}
                gor[gr] |= {a}
                quad[(gr // 3) * 3 + vr // 3] |= {a}
                temp.remove(x)
                # print('deep', deep)
                # print('2ss', x, pot[x], a)
                # print('quad', quad)
                # print('vert', vert)
                # print('gor', gor)
                # print('temp', temp)
                # print('acc', acc[1], acc[2], acc[3], acc[4], acc[5], acc[6])
                # print('filled', filled)
            else:
                return b
    return [0]

board =[[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
# board=[[".",".",".","7","4","8","6","3","2"],[".",".",".","6","5","2","4","1","9"],["4",".",".",".","3","9","8","7","5"],[".","5","7",".",".","6","2","4","1"],["2","6","4","3",".","7","5","9","8"],["1","9","8","5","2",".","3","6","7"],["9","7","5","8","6","3",".","2","4"],["8","3","2","4","9","1","7","5","6"],["6","4","1","2","7","5","9","8","3"]]
vert={i:{1,2,3,4,5,6,7,8,9} for i in range(9)}
gor={i:{1,2,3,4,5,6,7,8,9} for i in range(9)}
quad={i:{1,2,3,4,5,6,7,8,9} for i in range(9)}
pot={i:{1,2,3,4,5,6,7,8,9} for i in range(81)}
n=9
temp=set()
for i in range(n):
    for j in range(n):
        if board[i][j]!=".":
            pot[i*9+j]=set()
            temp.add(i*9+j)
            vert[j]-={int(board[i][j])}
            gor[i]-= {int(board[i][j])}
            quad[(i//3)*3+j//3]-= {int(board[i][j])}
for i in range(n):
    for j in range(n):
        if pot[i*9+j]:
            pot[i*9+j]=quad[(i//3)*3+j//3] & vert[j] & gor[i]
acc={i:set() for i in range(10)}
filled=dict()

for k in range(n**2):
    acc[len(pot[k])].add(k)
# print(acc)
b=solver(vert,gor,quad,pot,acc,filled,temp,board,0)
fin=b[1]

for k in fin.keys():
    i=k//9
    j=k%9
    board[i][j]=str(b[1][k])
for i in range(9):
    print(board[i])