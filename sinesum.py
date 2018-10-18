#!/usr/bin/env python3

import numpy as np

def s(t,n,T=(2*np.pi)):
    """s(t,n,T)

    """
    k = 1
    added = 0
    sum1 = 0
    list1 = []
    while True:
        added = (1/((2*k)-1)) * np.sin(((2*(2*k)-1)*np.pi * t)/T)
        sum1 = sum1 + added
        list1.append(sum1)
        if (k == n):
            break
        k += 1
    return ((4/np.pi)*sum1)

def f(t,T=(2*np.pi)):
    """f(t,T)
    t = test variable
    T = domain demonstrating variable

    returns 1,0 or -1 depending on t's relation to T
    """
    if (t > 0) and (t < T/2):
        return 1
    elif (t < 0) and (t > -T/2):
        return -1
    elif (t == 0):
        return 0
    else:
        print('t is not in the domain, please try again.')

print(s((np.pi),1000,(2*np.pi)))