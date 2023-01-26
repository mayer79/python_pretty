import math


def pretty(lo, up, n=5):
    """ Pretty bin boundaries.

    Returns pretty bin bounderies of about size n that covers the range from 
    lo to up. Simplified version of R's pretty().

    See implementations here:
    https://stackoverflow.com/questions/43075617/python-function-equivalent-to-rs-pretty
    And the R original https://github.com/wch/r-source/blob/trunk/src/appl/pretty.c

    Parameters
    ----------
    lo : float or int
        Lowest value to be covered.
    hi : float or int
        Highest value to be covered.
    n : int, optional
        Approximate number of intervals.

    Returns
    -------
    List of about n breaks covering the interval [lo, hi].

    Examples
    --------
    pretty(-1, 101, n=5)
    [-20, 0, 20, 40, 60, 80, 100, 120]
    
    """
    cell = (up - lo) / n
    base = 10 ** math.floor(math.log10(cell))
    if cell <= base * 1.4:
        k = 1
    elif cell <= base * 2.8:
        k = 2
    elif cell <= base * 7:
        k = 5
    else:
        k = 10
    unit = k * base
    ns = math.floor(lo / unit + 1e-10)
    nu = math.ceil(up / unit - 1e-10)

    return [unit * i for i in range(ns, nu + 1)]
