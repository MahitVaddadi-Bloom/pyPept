"""
NumPy compatibility layer for pyPept.

Ensures compatibility between NumPy 1.x and 2.x.
"""

import numpy as np
from packaging import version

# Check NumPy version
NUMPY_VERSION = version.parse(np.__version__)
NUMPY_2 = NUMPY_VERSION.major >= 2

# NumPy 2.0 changes some type aliases
if NUMPY_2:
    # In NumPy 2.0, some type aliases were removed
    # Use the new names if available
    try:
        np_int = np.int64
        np_float = np.float64
    except AttributeError:
        np_int = int
        np_float = float
else:
    # NumPy 1.x compatibility
    try:
        np_int = np.int_  # type: ignore
        np_float = np.float_  # type: ignore
    except AttributeError:
        np_int = np.int64
        np_float = np.float64


def asarray_compat(array_like, dtype=None):
    """
    Wrapper for np.asarray that handles dtype compatibility.
    
    Parameters
    ----------
    array_like : array_like
        Input data
    dtype : data-type, optional
        Data type
        
    Returns
    -------
    ndarray
        Array interpretation of array_like
    """
    if dtype is not None and isinstance(dtype, str):
        # Convert string dtype to actual dtype
        if dtype in ['int', 'int_']:
            dtype = np_int
        elif dtype in ['float', 'float_']:
            dtype = np_float
    
    return np.asarray(array_like, dtype=dtype)


__all__ = [
    'NUMPY_VERSION',
    'NUMPY_2',
    'np_int',
    'np_float',
    'asarray_compat',
]
