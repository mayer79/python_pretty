import math


def pretty(lo, up, n=5):
    """Pretty bin boundaries.

    Returns pretty bin bounderies of about size n that covers the range from
    lo to up. Simplified version of R's pretty().
    See implementations here:
    https://stackoverflow.com/questions/43075617/python-function-equivalent-to-rs-pretty
    And the R original https://github.com/wch/r-source/blob/trunk/src/appl/pretty.c

    Parameters
    ----------
    lo : float or int
        Lowest value to be covered.
    up : float or int
        Highest value to be covered.
    n : int, optional
        Approximate number of intervals.

    Returns
    -------
    List of about n breaks covering the interval [lo, up].

    Examples
    --------
    pretty(-1, 101, n=5)
    [-20, 0, 20, 40, 60, 80, 100, 120]
    """
    cell = (up - lo) / n
    base = 10 ** math.floor(math.log10(cell))
    r = cell / base
    if r <= 1.4:
        c = 1
    elif r <= 2.8:
        c = 2
    elif r <= 7:
        c = 5
    else:
        c = 10
    unit = c * base
    ns = math.floor(lo / unit + 1e-10)
    nu = math.ceil(up / unit - 1e-10)

    return [unit * i for i in range(ns, nu + 1)]
