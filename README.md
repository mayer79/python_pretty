# python_pretty

Classic algorithm to create pretty breaks for Python numpy arrays.

## Infos

Inspired by R's pretty() function, the Python script "pretty.py" implements the original
algorithm by W. J. Dixon and R. A. Kronmal (1965), "The choice of origin and scale for graphs", 
Journal of the ACM, 12(2):259-261.

Note that the function is different from the R implementation.

## Usage

```
import numpy as np
x = np.arange(1, 101)
pretty(x)                       # array([0., 20., 40., 60., 80., 100.])
pretty(x, n=4)                  # array([0., 50., 100., 150.])
pretty(x, base=5)               # array([0, 25, 50, 75, 100])
pretty(x, p=[10/7, 20/7, 50/7]) # array([0., 28.57142857, 57.14285714, etc.]
```

## Arguments

- x (np.array): Numpy array of size >= 2. Used to derive breaks.
- n (int, optional): Approximate number of intervals between breaks. Defaults to 5.
- p (list, optional): List of basic rounding numbers in [1, base),
    e.g. p = [10/7] will lead to multiples of 1/7, 10/7, 100/7 etc, 
    whatever fits best to "x" and "n". Defaults to [1, 2, 5].
- base (float, optional): Radix of the number system >= 2. Defaults to 10.0.
- tol (float, optional): Numeric tolerance for close 0 breaks. Defaults to 1e-9.
        