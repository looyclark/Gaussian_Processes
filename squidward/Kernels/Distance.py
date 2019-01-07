import numpy as np
from scipy.linalg import norm
import scipy.stats as st
from squidward.Utils import atleast_2d

def RBF(l, var_k):
    """
    """
    if l <= 0.0:
        raise Exception("Lengthscale parameter must be greater than zero")
    elif var_k <= 0.0:
        raise Exception("Kernel variance parameter must be greater than zero")
    def dist(alpha, beta):
        alpha, beta = atleast_2d(alpha), (beta)
        d = np.sum((alpha - beta)**2)
        amp = -0.5/l**2
        return var_k * np.exp( amp*d )
    return dist