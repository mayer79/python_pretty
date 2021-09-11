import numpy as np
import math

def pretty(x, n=5, p=[1, 2, 5], base=10.0, tol=1e-9):
    """Pretty Breakpoints

    Args:
        x (np.array): Numpy array of size >= 2. Used to derive breaks.
        n (int, optional): Approximate number of intervals between breaks. Defaults to 5.
        p (list, optional): List of basic rounding numbers in [1, base),
            e.g. p = [10/7] will lead to multiples of 1/7, 10/7, 100/7 etc, 
            whatever fits best to "x" and "n". Defaults to [1, 2, 5].
        base (float, optional): Radix of the number system >= 2. Defaults to 10.0.
        tol (float, optional): Numeric tolerance for close 0 breaks. Defaults to 1e-9.

    Returns:
        np.array: One-dimensional numpy array with pretty breaks.

    Examples:
        import numpy as np
        x = np.arange(1, 101)
        pretty(x)                       # array([0., 20., 40., 60., 80., 100.])
        pretty(x, n=4)                  # array([0., 50., 100., 150.])
        pretty(x, base=5)               # array([0, 25, 50, 75, 100])
        pretty(x, p=[10/7, 20/7, 50/7]) # array([0., 28.57142857, 57.14285714, etc.]

    Reference:
        W. J. Dixon and R. A. Kronmal (1965), "The choice of origin and scale for graphs", 
        Journal of the ACM, 12(2):259-261
    """

    # Initialization and checks
    assert x.size >= 2
    assert base >= 2
    assert n >= 2
        
    A = x.min()
    B = x.max()
    R = B - A
    assert R > 0

    n = int(n)

    p = np.sort(np.array(p))
    p = p[(p >= 1) & (p < base)]
    assert p.size >= 1

    # Begin calculations
    ti = math.floor(math.log(R / n) / math.log(base))

    if R / n / base**ti <= p.max():
        k = ti
    else:
        k = ti + 1

    i = np.where(p >= R / n / base**k)[0][0] + 1
    
    # Until scale is large enough
    b = B - 1
    while B > b:
        s = p[i - 1] * base**k
        a = s * math.floor(((B + A) / 2 - s * n / 2) / s)
        b = a + s * n
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