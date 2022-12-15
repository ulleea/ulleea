"""Импортируем нужные пакеты"""
import numpy as np
import scipy.linalg as lnlg

"""Составляем систему уравнений: матрицу A и вектор b"""

import numpy as np
n=21
A = np.zeros((21,21))
f=np.zeros(21)
f[0]+=1
for i in range(1,n-1):
    f[i]=f[i]+2/(i+1)**2
f[n-1]=f[n-1]-20/3
print(f)
A[0][0]+=1
for i in range(1,n-1):
    for j in range(n-1):
        if i==j:
            A[i][j]-=2
            A[i][j-1]+=1
            A[i][j+1]+=1
A[n-1][0]+=1
A[n-1][n-1]=1
for i in range(1,n-1):
    A[n-1][i]+=2
print(A)
n=100
b=f
print("Детерминант матрицы A:", np.linalg.det(A))
"""Выполняется LU разложение"""
lu, piv = lnlg.lu_factor(A)
x = lnlg.lu_solve((lu, piv),b)
r = np.dot(A, x) - b
"""Считаем невязки"""
r_1 = max(r)
r_2 = sum(abs(r))
r_3 = np.sqrt(sum(i*i for i in r))
print(
      "Решение x:\n", x,
      "\nНайденные невязки:\n",
      " r_1: {0:.2e}\n".format(r_1),
      " r_2: {0:.2e}\n".format(r_2),
      " r_3: {0:.2e}\n".format(r_3),
     )

"""Ищем lambda_max"""

eps = 1e-4
r = b
converge = False
while not converge:
    r_upd = (A.dot(r)) / np.sqrt(sum([i**2 for i in A.dot(r)]))
    converge = (np.sqrt(sum([i**2 for i in r_upd - r])) <= eps)
    r = r_upd

lambda_max = (r.T @ A @ r) / (r.T @ r)
print('--------------')
print('lmax=',lambda_max)
print('==============')
"""Ищем lambda_min"""

eps = 1e-4
r = b
converge = False
while not converge:
    B = lambda_max * np.eye(n) - A
    r_upd = B.dot(r) / np.sqrt(sum([i**2 for i in B.dot(r)]))
    converge = (np.sqrt(sum([i**2 for i in r_upd - r])) <= eps)
    r = r_upd

lambda_min = (r.T @ A @ r) / (r.T @ r)
print('lmin=',abs(lambda_min))
print("Число обусловленности: ", abs(lambda_max/lambda_min))
# q,w=np.linalg.eigh(A, UPLO='L')
# # print(q)
# for lamb in q:
#     R=A
#     for i in range(n):
#         for j in range(n):
#             if i<=j:
#                 R[i][j]=R[i][j]*lamb
#     if np.linalg.det(A)==0 and abs(lamb)>1:
#         print(lamb)
#
# print('выше перечисленны собственные значения>1 по модулю, если на них домножить элементы матрицы лежищие не выше главной диагонали, то детерминант полученной матрицы будет равен нулю')
# print('отсюда следует, что метод зейделя не сходится')

"""Ищем решение методом Зейделя"""

s = len(A)
x = b
Iteration = 0
converge = False
pogr = 0.
while not converge:
    x_upd = np.copy(x)
    for i in range(s):
        s1 = sum(A[i][j] * x_upd[j] for j in range(i))
        s2 = sum(A[i][j] * x[j] for j in range(i + 1, s))
        x_upd[i] = (b[i] - s1 - s2) / A[i][i]
    pogr = np.sqrt(sum((x_upd[i] - x[i])**2  for i in range(s)))
    converge =  pogr < 1e-4
    Iteration += 1
    x = x_upd
print('Количество итераций :', Iteration)
print('Решение системы уравнений :', x)
print('Погрешность :', pogr)
