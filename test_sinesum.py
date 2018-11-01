#!/usr/bin/env python3

import numpy as np
import sinesum

"""sinesum.py Test Module

Verify implementation of the Fourier sine series using numpy arrays.
"""

def test_s():
    """this def tests the function s in the module sinesum, if it returns the right value"""
    assert 0.99 < sinesum.s((0.5*np.pi),100000,(2*np.pi)) <=1
    
    
def test_f():
    """ this def tests the function f in the module sinesum, it will return the right value"""
    np.testing.assert_almost_equal(sinesum.f(0.5*np.pi,2*np.pi),1)
    
