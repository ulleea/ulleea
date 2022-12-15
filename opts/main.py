import matplotlib.pyplot as plt
import numpy as np

#from scipy import misc
#enot = (misc.face(gray = True)/255)[:, -768:]

mox = plt.imread('mox.jpg')[::3, ::3, :] / 255
image = mox
print(image.shape)

# plt.imshow(image)
# # plt.axis('off')
# plt.show()

#Denoising problem

plt.figure(figsize=(12,5))
x0 = np.clip(image +   0.6*(np.random.random(image.shape) - 0.5), 0, 1)

# plt.imshow(x0)
# plt.axis('off')
# plt.show()


smooth_eps = 1e-3


# plt.subplot(122)
# plt.plot(x, x / (x**2 + smooth_eps)**0.5)
# plt.title('derivative of smoothed norm')

#How to implement?
#Wrong approach - in python loops

# x = image
# m, n, k = x.shape
# tv = 0
# for i in range(1, m):
#     for j in range(1, n):
#         tv += ((x[i, j] - x[i, j - 1]) ** 2 + (x[i, j] - x[i - 1, j]) ** 2) ** 0.5


def TV(x):
    # print(x.shape)
    TV = ((smooth_eps + (x - np.roll(x, 1, axis=0)) ** 2 + (x - np.roll(x, 1, axis=1)) ** 2) ** 0.5)
    return np.sum(TV)


# print(TV(x))

def dTV(x):
    x_diff = x - np.roll(x, -1, axis=1)
    y_diff = x - np.roll(x, -1, axis=0)
    grad_norm2 = x_diff ** 2 + y_diff ** 2 + smooth_eps
    dgrad_norm = 0.5 / np.sqrt(grad_norm2)
    dx_diff = 2 * x_diff * dgrad_norm
    dy_diff = 2 * y_diff * dgrad_norm
    grad = dx_diff + dy_diff
    grad[:, 1:, :] -= dx_diff[:, :-1, :]
    grad[1:, :, :] -= dy_diff[:-1, :, :]
    return grad


# print(dTV(x))

# dTV is taken from https://gist.github.com/crowsonkb/ddf8167359be4ba2aa34835aa207e241

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

alpha = 2

def f(x, x0):
    return TV(x) + alpha * np.linalg.norm(x - x0)


def df(x, x0):
    return dTV(x) + alpha * 2 * (x - x0)


lf, ldf = Logger(f), Logger(df)

def alpha_cal(f,df,x,alpha0,d,k=0.5):
    alpha=alpha0
    while f(x+alpha*(d)) > np.sum(0.3*alpha*(-d**2)) + f(x):
        alpha*=k
    return alpha

def gd(f, df, h, x0, m,niter=20,alpha=0.3, rho=0.8):
    x = x0
    for i in range(m):
        # print(i)
        # print(h)
        h /= (i + 1) ** 0.5
        tr = f(x)
        x -= h * df(x)
        # valueoffunc.append(TV(x))
    for i in range(niter-m):
        # print(i)
        d=-df(x)
        xk=x + alpha_cal(f,df,x,alpha,d)*(d)
        x=xk
    valueoffunc.append(TV(x))
    ms.append(m/niter)

    return x

x0 = np.clip(image + 0.6*(np.random.random(image.shape) - 0.5), 0, 1)
valueoffunc=[]
lf.reset(), ldf.reset()
grad = lambda x : ldf(x, x0)
fun = lambda x : lf(x, x0)
# x = gd(fun, grad, 0.1, x0,0, niter=25)
#
# plt.figure(figsize=(15,8))
# plt.imshow(x, cmap='gray')
# print(np.linalg.norm(df(x, x0)), f(x, x0))
# plt.show()
# plt.figure(figsize=(12,4))
# plt.subplot(121)
# flog_ = np.array(lf.log)
# flog = [flog_[0]]
# for f in flog_[1:]:
#     if f < flog[-1]:
#         flog.append(f)
# x = np.arange(1, len(flog) +1 )
# yref = (flog[0] - flog[-1])/x**1.0 + flog[-1]
q = 1
def scale(y):
    return y
# plt.plot(scale(flog), label='$f_k$')
# plt.plot(scale(yref), label='$(f_0 - f_*)/k$')
# plt.xlabel('k')
# plt.ylabel('f')
# plt.legend()
# plt.subplot(122)
# plt.plot(ldf.log, label='$||df||$')
# plt.xlabel('k')
# plt.ylabel('$||df||$')
# plt.legend()


np.random.seed(228)
# smooth_eps = 1e0
corrupted_mask = np.random.random(image.shape[:2]) < 0.98
corrupted_mask = np.expand_dims(corrupted_mask, 2)

x0_paint = image * (np.logical_not(corrupted_mask))  # + 0.4 * np.random.random(image.shape) * corrupted_mask


def df_paint(x):
    return dTV(x) * corrupted_mask


lf_paint = Logger(TV)
ldf_paint = Logger(df_paint)

# plt.figure(figsize=(16, 8))
# plt.subplot(121)
# plt.imshow(x0_paint)
ms=[]
num=250
m=0

for j in range(0,num,10):
    h=0.5
    painted = gd(lf_paint, ldf_paint, h, x0_paint, j,500,)

plt.plot(ms,valueoffunc)
plt.title('N=500')
plt.xlabel('m/N')
plt.ylabel('f(x)')
plt.grid()
plt.show()

# plt.subplot(122)
# plt.imshow(painted)
# plt.show()
# plt.figure(figsize=(12,4))
# plt.subplot(121)
# flog_ = np.array(lf_paint.log)
# flog = [flog_[0]]
# for f in flog_[1:]:
#     if f < flog[-1]:
#         flog.append(f)
# flog = np.array(flog)
# flog = np.array(lf_paint.log)#[:100]
# x = np.arange(1, len(flog) +1 )
# yref = 150*(flog[0] - flog[-1])/(x+4) + flog[-1]

# q = 1
# def scale(y):
    # return (y ** (q))#[-len(y)//10:]
# plt.plot(scale(flog), label='f')
# plt.plot(scale(yref)[100:], label='ref')
# plt.legend()
# plt.subplot(122)
# plt.plot(ldf_paint.log, label='df')
# plt.legend()