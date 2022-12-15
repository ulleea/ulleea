import numpy as np

n=99
A = np.zeros((100, 101))
f = (np.arange(n+1) + 1)
print(f)
A[0, 0:2] = [10, 1]
A[n, 0:n+1] = np.ones(n+1)
for i in range(100):
    A[i, 0:i+5] = 1
    A[i, i] = 2

for i in range(1, 100):
    A[i, 0:max(i-4, 0)] = 0
    A[:, -1] = f
print(A, 'расширенная исходная матрица')

from scipy.linalg import lu
p, L, U = lu(A[:, :-1])
b = A[:, -1]
A = A[:, :-1]
print('=======')
print('A=',A)

print('b=',b)

y = np.zeros(n+1)
y[0] = b[0]
for i in range(1, n+1):
    y[i] = b[i] - L[i, 0:i] @ y[:i]

x = np.zeros(n+1)
x[n] = y[n]/U[n, n]
for i in range(1, n+1):
    x[n-i] = (y[n-i] - U[n-i, :] @ x) / U[n-i, n-i]
print('x=',x)
print(len(x))
print('=======')
print(A @ x)

print(b)
print('==============')

print('----------------------------')

# # zeidel
# def seidel(A, x, b):
#     n = len(A)
#     for j in range(0, n):
#         d = b[j]
#
#         for i in range(0, n):
#             if (j != i):
#                 # print('--')
#                 # print(i,j)
#                 # print('==')
#                 # if A[j][i]==0 or x[i]==0:
#                 #     print(A[j][i],x[i])
#                 d -= A[j][i] * x[i]
#         x[j] = d / A[j][j]
#     return x
#
#
# x = np.zeros(n + 1)
# x_prev = np.ones(n + 1) + 10
# while np.linalg.norm(x - x_prev) >= 1e-4:
#     x_prev = np.copy(x)
#     x = seidel(A, x, b)

# """Ищем решение методом Зейделя"""
#
# s = len(A)
# x = b
# Iteration = 0
# converge = False
# pogr = 0.
# while not converge:
#     x_upd = np.copy(x)
#     for i in range(s):
#         s1 = sum(A[i][j] * x_upd[j] for j in range(i))
#         s2 = sum(A[i][j] * x[j] for j in range(i + 1, s))
#         x_upd[i] = (b[i] - s1 - s2) / A[i][i]
#     pogr = np.sqrt(sum((x_upd[i] - x[i])**2  for i in range(s)))
#     converge =  pogr < 1e-4
#     Iteration += 1
#     x = x_upd
# print('Количество итераций :', Iteration)
# print('Решение системы уравнений :', x)
# print('Погрешность :', pogr)

print('x=',x)
print(A@x)

#chisloobuslovlennosti
r = np.ones(n+1).reshape(-1, 1)
B = A.T @ A
for i in range(100):
    r = (B @ r) / (np.linalg.norm(B @ r))
    lambda_max = (r.T @ B @ r) / (r.T @ r)
print('lmax=',lambda_max)
C = B - lambda_max * np.eye(n+1)
r = np.ones(n+1).reshape(-1, 1)
for i in range(100):
    r = (C @ r) / (np.linalg.norm(C @ r))
    jj = (r.T @ C @ r) / (r.T @ r)
lambda_min = lambda_max + jj
print('lmin=',lambda_min)
print(np.sqrt(lambda_max/lambda_min))
np.linalg.cond(A)