def trainfun(portfolio,array,g,j):
    if j!=0:
        n=len(array)
        for i in range(n):
            array[i][1]+=g[array[i][0]][1][j]-g[array[i][0]][1][j-1]
    array=sorted(array, key=lambda intege: intege[1])
    return portfolio,array[::-1]