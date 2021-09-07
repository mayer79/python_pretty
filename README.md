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
pretty(x)                  # array([  0,  10,  20,  30,  40,  50,  60,  70,  80,  90, 100])
pretty(x, nint=4)          # array([  0,  40,  80, 120])
pretty(x, base=5, nint=4)  # array([  0,  25,  50,  75, 100])
```

## Arguments

- x (np.array): One-dimensional numpy array. Used to derive breaks.
- nint (int, optional): Approximate number of intervals. Defaults to None.
- p (list, optional): List of basic round numbers between 1 and "base",
            e.g. p = 10/7 will lead to multiples of 1/7, 10/7, 100/7 etc, 
            whatever fits best to "x" and "nint". Defaults to None.
- base (int, optional): Radix of the number system. Defaults to 10.
        