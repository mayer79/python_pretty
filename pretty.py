import numpy as np
import math

def pretty(x, nint=None, p=None, base=10, tol=1e-9):
    """Pretty Breakpoints

    Args:
        x (np.array): Numpy array of size >= 2. Used to derive breaks.
        nint (int, optional): Approximate number of intervals between breaks. Defaults to None.
            In this case, nint is calculated from the size of x.
        p (list, optional): List of basic rounding numbers >= 1 and < "base",
            e.g. p = [10/7] will lead to multiples of 1/7, 10/7, 100/7 etc, 
            whatever fits best to "x" and "nint". Defaults to None.
        base (int, optional): Radix of the number system >= 2. Defaults to 10.
        tol (float, optional): Numeric tolerance for determining if small breaks are 0.

    Returns:
        np.array: One-dimensional numpy array with pretty breaks.

    Examples:
        import numpy as np
        x = np.arange(1, 101)
        pretty(x)                  # array([  0,  10,  20,  30,  40,  50,  60,  70,  80,  90, 100])
        pretty(x, nint=4)          # array([  0,  40,  80, 120])
        pretty(x, base=5, nint=4)  # array([  0,  25,  50,  75, 100])
        pretty(x, p=[10/7])        # array([  0., 14.28571429, 28.57142857, etc.]

    Reference:
        W. J. Dixon and R. A. Kronmal (1965), "The choice of origin and scale for graphs", 
        Journal of the ACM, 12(2):259-261
    """

    assert x.size >= 2
    assert isinstance(base, int)
    assert base >= 2
        
    A = x.min()
    B = x.max()
    R = B - A

    assert R > 0

    if not nint:
        nint = min(math.floor(base * math.log(x.size) / math.log(base)), 10)

    if p is None:
        p = np.arange(1, base)
    else:
        p = np.sort(np.array(p))
        assert p[0] >= 1 and p[-1] < base

    ti = math.floor(math.log(R / nint) / math.log(base))

    if R / nint / base**ti <= p.max():
        k = ti
    else:
        k = ti + 1

    i = np.where(p >= R / nint / base**k)[0][0] + 1
    
    # Until scale is large enough
    b = B - 1
    while B > b:
        s = p[i - 1] * base**k
        a = s * math.floor(((B + A) / 2 - s * nint / 2) / s)
        b = a + s * nint
        if i < p.size:
            i += 1
        else:
            i = 1
            k += 1

    # Organize output
    out = np.arange(a, b + 1, s)
    out = out[(out >= A - s) & (out <= B + s)]
    out[abs(out) < tol] = 0

    return out