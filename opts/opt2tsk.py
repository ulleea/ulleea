import matplotlib.pyplot as plt
import numpy as np


mox = plt.imread('mox.jpg')[::3, ::3, :]
image = mox
# print('---')
# print(image.shape)
# print('---')
# plt.imshow(image)
# plt.axis('off')
# plt.show()
# print('---------',np.random.random(image.shape))
# plt.figure(figsize=(12,5))
x0 = np.clip(image +   0.6*(np.random.random(image.shape) - 0.5), 0, 1)

# plt.imshow(x0)
# plt.axis('off')
# plt.show()

smooth_eps = 1e-3
# plt.figure(figsize=(14,4))
x = np.linspace(-1e-1, 1e-1, 100)
# plt.subplot(121)
# plt.plot(x, (x**2 + smooth_eps)**0.5, label='smoothed $l_2$ norm')
# plt.plot(x, (x**2)**0.5, label='$l_2$ norm')
# plt.title('$l_2$ norm smoothing')
# plt.legend()
# plt.show()

# def TVsq_matrix(x):
    #your code

def TV(x):
    tv=(((np.roll(x, 1, axis=0) - x) ** 2 + (np.roll(x, 1, axis=1) - x) ** 2 + smooth_eps) ** 0.5)
    tv=tv[:-1, :-1]
    tv = np.sum(tv)
    # print(tv)
    return tv


def dTV(x):
    dx = x - np.roll(x, -1, axis=1)
    dy = x - np.roll(x, -1, axis=0)
    # print(dx)
    # print('---')
    # print(dy)
    # print('===')
    gradnorm1 = dx *dx + dy*dy + smooth_eps
    sqr=np.sqrt(gradnorm1)
    dgradnorm2 = 0.5 / sqr

    dx1 = 2 * dx * dgradnorm2
    dy2 = 2 * dy * dgradnorm2


    grad = dx1 + dy2
    grad[:, 1:, :] -= dx1[:, :-1, :]
    grad[1:, :, :] -= dy2[:-1, :, :]
    return grad

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


def gd(f, df, h, x0, niter=300, alpha=0.3, rho=0.8, armijo=False):
    x = x0
    if armijo:
        for i in range(niter):
            print(i)
            while (f(x) - (f(x - h * df(x)) + alpha * h * np.sum(df(x) * df(x)))) < 0:

                h *= rho
                print(h)
            x -= h * df(x)
    else:
        for i in range(niter):
            # print(i)
            # print(h)
            h /= (i + 1) ** 0.5
            tr = f(x)
            x -= h * df(x)
    return x

lf.reset(), ldf.reset()
grad = lambda x : ldf(x, x0)
fun = lambda x : lf(x, x0)
x = gd(fun, grad, 0.1, x0, niter=300)



print('adfgjhadkjfhaldskj')
plt.figure(figsize=(15,8))
plt.imshow(x, cmap='gray')
# print(np.linalg.norm(df(x, x0)), f(x, x0))
plt.show()
print('adshfhadjfsh')
plt.figure(figsize=(12,4))
plt.subplot(121)
print('----')
flog_ = np.array(lf.log)


print('----')


flog = [flog_[0]]
for f in flog_[1:]:
    if f < flog[-1]:
        flog.append(f)
x = np.arange(1, len(flog) +1 )
yref = (flog[0] - flog[-1])/x**1.0 + flog[-1]
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
# plt.show()

np.random.seed(228)
# smooth_eps = 1e0
corrupted_mask = np.random.random(image.shape[:2]) < 0.98
corrupted_mask = np.expand_dims(corrupted_mask, 2)

x0_paint = image * (np.logical_not(corrupted_mask))  # + 0.4 * np.random.random(image.shape) * corrupted_mask


def df_paint(x):
    return dTV(x) * corrupted_mask


lf_paint = Logger(TV)
ldf_paint = Logger(df_paint)

plt.figure(figsize=(16, 8))
plt.subplot(121)
plt.imshow(x0_paint)

painted = gd(lf_paint, ldf_paint, 0.1, x0_paint, 3000, armijo=True)

plt.subplot(122)
plt.imshow(painted)
plt.title("Армихо")
plt.show()

plt.figure(figsize=(12,4))
plt.subplot(121)
flog_ = np.array(lf_paint.log)
flog = [flog_[0]]
for f in flog_[1:]:
    if f < flog[-1]:
        flog.append(f)
flog = np.array(flog)
# flog = np.array(lf_paint.log)#[:100]
x = np.arange(1, len(flog) +1 )
yref = 150*(flog[0] - flog[-1])/(x+4) + flog[-1]

q = 1
def scale(y):
    return (y ** (q))#[-len(y)//10:]
plt.plot(scale(flog), label='f')
# plt.plot(scale(yref)[100:], label='ref')
plt.legend()
plt.subplot(122)
plt.plot(ldf_paint.log, label='df')
plt.legend()