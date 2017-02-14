# -*- coding: utf-8 -*-

import numpy as np
import time

#Local Imports
from cpu_lib import binary_search as cpu_search
from cu_lib_import import binary_search as gpu_search







# Set an array size to create
arr_len = 1e009


# Dummy array created
arr = np.arange(0, arr_len, 1).astype("i4")

# Random search value chosen
search = np.random.randint(0, arr_len)
print("Searching for integer %i...") % search

# GPU search function call
t0 = time.time()
res_gpu = gpu_search(arr, len(arr), search)
print("Total GPU Time: %i ns") % ((time.time() - t0)*1e009)

# CPU search function call
t0 = time.time()
res_cpu = cpu_search(arr, search)
print("Total CPU Time: %i ns") % ((time.time() - t0)*1e009)

