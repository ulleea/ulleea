import matplotlib.pyplot as plt
import numpy as np
import time
class Logger:
    def __init__(self, f):
        self.f = f
        self.calls = 0
        self.log = []

    def __call__(self, *args):
        self.calls += 1
        val = self.f(*args)
        self.log.append(np.linalg.norm(val))
        return val

    def reset(self):
        self.calls = 0
        self.log = []

def f(x, x0):
    return TV(x) + alpha * np.linalg.norm(x - x0)


def df(x, x0):
    return dTV(x) + alpha * 2 * (x - x0)


lf, ldf = Logger(f), Logger(df)

alpha = 2
mox = plt.imread('mox.jpg')[::3, ::3, :] / 255
image = mox

plt.imshow(image)
# plt.axis('off')
plt.show()
plt.figure(figsize=(12,5))
x0 = np.clip(image +   0.6*(np.random.random(image.shape) - 0.5), 0, 1)

plt.imshow(x0)
plt.axis('off')
plt.show()
smooth_eps = 1e-3
plt.figure(figsize=(14,4))
x = np.linspace(-1e-1, 1e-1, 100)
plt.subplot(121)
plt.plot(x, (x**2 + smooth_eps)**0.5, label='smoothed $l_2$ norm')
plt.plot(x, (x**2)**0.5, label='$l_2$ norm')
plt.title('$l_2$ norm smoothing')
plt.legend()
time=time.time()
x = image
m, n, k = x.shape
tv = 0
for i in range(1, m):
    for j in range(1, n):
        tv += ((x[i, j] - x[i, j-1])**2 + (x[i, j] - x[i-1, j])**2)**0.5




