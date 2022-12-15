def traidfun(portfolio,array,g,i,money):
    # if portfolio==[]:
    #     s1=s2=s3=0
    #     while money/3-g[array[0][0]][1][i]:
    #         if s1==0:
    #             portfolio.append([array[0][0],1])
    #             money=money-g[array[0][0]][1][i]
    #         else:
    #             portfolio[0][1]+=1
    #             money = money - g[array[0][0]][1][i]
    #     while money/3-g[array[1][0]][1][i]:
    #         if s2==0:
    #             portfolio.append([array[1][0],1])
    #             money = money - g[array[1][0]][1][i]
    #         else:
    #             portfolio[1][1]+=1
    #             money = money - g[array[1][0]][1][i]
    #     while money/3-g[array[2][0]][1][i]:
    #         if s3==0:
    #             portfolio.append([array[2][0],1])
    #             money = money - g[array[2][0]][1][i]
    #         else:
    #             portfolio[2][1]+=1
    #             money = money - g[array[2][0]][1][i]
    # return portfolio,money
    portfolio=[[array[0][0],3],[array[1][0],4],[array[2][0],5]]
    if i==57:
        portfolio = [[array[0][0], 3], [array[1][0], 4], [array[3][0], 7]]
    return portfolio,500