def norm(a):
    return np.sqrt(np.sum((np.square(a)),axis=1))
import numpy as np

a=np.arange(15)[::-1].reshape((3, 5))
n=len(a)
print(a)
# print(a[0,:])
b=np.arange(10).reshape((2,5))
print()
print(b)

dists=np.sqrt(np.sum((a[:,None]-b)**2,axis=-1))
# print(a[:,None]-b)
print(dists)
print(np.transpose(a))
q=dists.min(axis=0)
p=dists.min(axis=1)
# print(q)
# print(p)
k=2
print()
print(dists[1,:])
print()
# print(np.partition(dists[:,0],k,axis=0)[:k])
# print(np.partition(dists[:,1],k,axis=0)[:k])
# r=np.argpartition(dists,k,axis=0)[:k,:]
# # print()
# print(r)
# print()
# print(np.argpartition(dists[:,1],k,axis=0))
# print('=====')
# a=np.arange(10)[::-1]
# print(a)
# b=np.zeros((3,4))
# print(b)
# print('==')
# c=np.array([0])
# b[1,:]=a[c]
# print(b)
# print(r[:,1][0])
# q=np.zeros((2,2))
# q[1,:]=r[:,1]
# print()
print()
# for i in range(2):
#     for j in range(k):
print('=======-=')
a = np.array([1.,2.,3.,1.,2.,1.,1.,1.,3.,2.,2.,1.])
counts = np.bincount(a.astype(np.int64))
print(a[:None])
#
# # print()
# # print(r[:k])
#
# # def compute_distances_two_loops(self, X_test):
# #     import numpy as np
# #     n = len(X_test)
# #     a = np.zeros((n, n))
# #     for i in range(n):
# #         for j in range(n):
# #             a[i][j] = np.sqrt(np.sum(np.square(X_test[i] - X_test[j])))
# #     return a
# #
# # def compute_distances_one_loop(self,X_test):
# #     import numpy as np
# #     n = len(X_test)
# #     for i in range(n):
# #         if i == 0:
# #                 c = self.norm(np.subtract(X_test, X_test[i]))
# #         else:
# #             b = self.norm(np.subtract(X_test, X_test[i]))
# #             c = np.column_stack([c, b])
# #     return c
# # def compute_distances_no_loops(self):
# #     a = np.sqrt(np.sum((X_test[:, None] - X_test) ** 2, axis=-1))
# #     return a
# print('--=-')
# n=3
# k=1
# a=np.array([1,2,3])
# print(a[:1])
# print(np.zeros((n,k)))
