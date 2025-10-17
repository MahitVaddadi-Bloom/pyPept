"""
pyPept: A Python library for peptide analysis and manipulation.
"""

__version__ = "1.0.0"

import importlib.metadata

try:
    __version__ = importlib.metadata.version(__package__ or __name__)
except importlib.metadata.PackageNotFoundError:
    # Package is not installed, use fallback version
    pass

__all__ = ["__version__"]


