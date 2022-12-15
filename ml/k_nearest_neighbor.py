import sys

import numpy as np
import unittest
import time

import collections
import pickle
import io


class KNearestNeighbor:


    def __init__(self):
        pass

    def fit(self, X, y):

        self.X_train = X
        self.y_train = y

    def predict(self, X, k=1, num_loops=0):

        if num_loops == 0:
            dists = self.compute_distances_no_loops(X)
        elif num_loops == 1:
            dists = self.compute_distances_one_loop(X)
        elif num_loops == 2:
            dists = self.compute_distances_two_loops(X)
        else:
            raise ValueError('Invalid value %d for num_loops' % num_loops)

        return self.predict_labels(dists, k=k)

    def compute_distances_two_loops(self, X):

        num_test = X.shape[0]
        num_train = self.X_train.shape[0]
        dists = np.zeros((num_test, num_train))
        for i in range(num_test):
            for j in range(num_train):

                dists[i,j] = np.sqrt(np.sum(np.square(X[i] - self.X_train[j])))

        return dists

    def compute_distances_one_loop(self, X):

        num_test = X.shape[0]
        num_train = self.X_train.shape[0]
        dists = np.zeros((num_test, num_train))
        for i in range(num_test):

            dists[i,:]=np.sqrt(np.sum((np.subtract(self.X_train,X[i]))**2, axis=1))

        return dists

    def compute_distances_no_loops(self, X):

        num_test = X.shape[0]
        num_train = self.X_train.shape[0]
        dists = np.zeros((num_test, num_train))

        dists = np.sqrt(np.sum((X[:, None] - self.X_train) ** 2, axis=-1))

        return dists

    def predict_labels(self, dists, k=1):

        num_test = dists.shape[0]
        y_pred = np.zeros(num_test)
        for i in range(num_test):
            sort_dist = np.argsort(dists[i])
            closest_y = self.y_train[sort_dist[0:k]]
            y_pred[i] = np.argmax(np.bincount(closest_y.astype(np.int64)))
        return y_pred


from sklearn import datasets
dataset = datasets.load_digits()
# print(dataset.DESCR)
test_border = 100
X_train, y_train = dataset.data[test_border:], dataset.target[test_border:]
X_test, y_test = dataset.data[:test_border], dataset.target[:test_border]

print('Training data shape: ', X_train.shape)
print('Training labels shape: ', y_train.shape)
print('Test data shape: ', X_test.shape)
print('Test labels shape: ', y_test.shape)
num_test = X_test.shape[0]
print(num_test,'num_test')
import random
import numpy as np
import matplotlib.pyplot as plt



plt.rcParams['figure.figsize'] = (14.0, 12.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

classes = list(np.arange(10))
num_classes = len(classes)
samples_per_class = 7
for y, cls in enumerate(classes):
    idxs = np.flatnonzero(y_train == y)
    idxs = np.random.choice(idxs, samples_per_class, replace=False)
    for i, idx in enumerate(idxs):
        plt_idx = i * num_classes + y + 1
        plt.subplot(samples_per_class, num_classes, plt_idx)
        plt.imshow(X_train[idx].reshape((8, 8)).astype('uint8'))
        plt.axis('off')
        if i == 0:
            plt.title(cls)
# plt.show()
classifier = KNearestNeighbor()
classifier.fit(X_train, y_train)
dists = classifier.compute_distances_two_loops(X_test)
print(dists.shape,'--')
plt.imshow(dists, interpolation='none')
# plt.show()
y_test_pred = classifier.predict_labels(dists, k=1)
num_correct = np.sum(y_test_pred == y_test)
accuracy = float(num_correct) / num_test
print('Got %d / %d correct => accuracy: %f' % (num_correct, num_test, accuracy))
y_test_pred = classifier.predict_labels(dists, k=5)
num_correct = np.sum(y_test_pred == y_test)
accuracy = float(num_correct) / num_test
print('Got %d / %d correct => accuracy: %f' % (num_correct, num_test, accuracy))
dists_one = classifier.compute_distances_one_loop(X_test)

difference = np.linalg.norm(dists - dists_one, ord='fro')
print('One loop difference was: %f' % (difference, ))
if difference < 0.001:
    print('Good! The distance matrices are the same')
else:
    print('Uh-oh! The distance matrices are different')
    dists_two = classifier.compute_distances_no_loops(X_test)

    difference = np.linalg.norm(dists - dists_two, ord='fro')
    print('No loop difference was: %f' % (difference,))
    if difference < 0.001:
        print('Good! The distance matrices are the same')
    else:
        print('Uh-oh! The distance matrices are different')


knn_test = KNearestNeighbor()
def time_function(f, *args):

    tic = time.time()
    output = f(*args)
    toc = time.time()
    return toc - tic, output

knn_test.fit(X_train, y_train)

np.random.seed(42)
two_loop_time, out_2_loops = time_function(knn_test.compute_distances_two_loops, X_test)