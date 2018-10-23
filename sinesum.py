#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def s(t, n, T=(2 * np.pi)):
    """s(t,n,T)

    """
    k = np.arange(1, n + 1)

    s = (1 / ((2 * k) - 1)) * np.sin((2 * ((2 * k) - 1) * np.pi * t) / T)
    return (4 / np.pi) * np.sum(s)


def splot(t, n, T=(2 * np.pi)):
    """splot(t,n,T)

    """
    k = np.arange(1, n + 1)

    s = (4 / np.pi) * (1 / ((2 * k) - 1)) * np.sin((2 * ((2 * k) - 1) * np.pi * t) / T)

    S = []
    for i in k:
        v = 0
        tot = 0
        while v < i - 1:
            tot = tot + s[v]
            v += 1
        S.append(tot)

    return S


def f(t, T=(2 * np.pi)):
    """f(t,T)
    t = test variable
    T = domain demonstrating variable

    returns 1,0 or -1 depending on t's relation to T
    """
    if (t > 0) and (t <= T / 2):
        return 1
    elif (t < 0) and (t >= -T / 2):
        return -1
    elif (t == 0):
        return 0
    else:
        print('t is not in the domain, please try again.')


def plot(t, n, T=(2 * np.pi)):
    """
    """
    S = splot(t, n, T)

    plt.grid()

    plt.xlim(0, n)

    return plt.plot(S)
