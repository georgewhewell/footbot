try:
    from .bigquery import *
except ImportError:
    from .hdf5 import *
