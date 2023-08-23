import numpy as np
from scipy.io import wavfile
from numpy.fft import fft, ifft, fftshift


def hamming(M):
    n = np.arange(M)
    return 0.54 - 0.46 * np.cos(2 * np.pi * n / (M - 1))


def hann(M):
    n = np.arange(M)
    return 0.5 - 0.5 * np.cos(2 * np.pi * n / (M - 1))


def rectwin(M):
    return np.ones(M)


def phase_voc(x, ts_ratio, L=1024, H=256, win=hamming):
    syn_hop = H * ts_ratio
    N = len(x)
    w = win(L)
    gain = 1. / (L * np.sum((win(L) * win(L))) / syn_hop)
    unwrapdata = 2 * np.pi * H / L * np.arange(0, L).T
    yangle, ysangle = np.zeros(L), np.zeros(L)
    ys = np.zeros(L, dtype=complex)
    yprevwin = np.zeros(L - syn_hop, dtype=complex)

    first_time = True
    y = np.array(0)

    for i in np.arange(0, N - L, H):

        yprevangle = yangle


        yfft = fft(w * x[i: i + L])
        ymag, yangle = np.abs(yfft), np.angle(yfft)


        yunwrap = (yangle - yprevangle) - unwrapdata
        yunwrap = yunwrap - np.round(yunwrap / (2. * np.pi)) * 2 * np.pi
        yunwrap = (yunwrap + unwrapdata) * ts_ratio

        if first_time:
            ysangle = yangle
            first_time = False
        else:
            ysangle += yunwrap


        ys.real, ys.imag = np.cos(ysangle), np.sin(ysangle)
        ys *= ymag
        ywin = ifft(w * ys)


        olapadd = np.hstack((ywin[:L - syn_hop] + yprevwin,
                             ywin[L - syn_hop:]))
        yistfft = olapadd[: syn_hop]
        yprevwin = olapadd[syn_hop:]


        yistfft = yistfft * gain
        y = np.hstack((y, yistfft))

    return y * np.max(np.abs(x)) / np.max(np.abs(y))


infile, tsfile, psfile = 'sent1.wav', 'out1.wav', 'out2.wav'
Fs, x = wavfile.read(infile)

import sys

scale = 2.
y = phase_voc(x, 2., L=1024, H=128, win=hamming)

wavfile.write(tsfile, Fs, np.array(y, dtype='int16'))
wavfile.write(psfile, Fs * scale, np.array(y, dtype='int16'))
_, x2 = wavfile.read(psfile)

