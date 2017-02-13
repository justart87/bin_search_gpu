# bin_search_gpu
An attempt at a binary search on the GPU. Unfortunately, GPUs are not ideal for this type of algorithm for a few reasons. For example, even a single H2D memory transfer takes longer than the time it takes to (typically) perform the full algorithm on a single CPU thread. Additionally, there is no intuitive way to parallelize the code in a manner that makes sense, when non-coalesced memory reads are very slow.

This code is just an example of how to split global memory on a GPU and perform some operations on it, and benchmark it against to the CPU.

### Compiling
In the main folder, run the following command in your Linux terminal:

`nvcc -arch=sm_30 -m64 -Xcompiler -fPIC -shared -o cu_binary_search.so binary_search.cu -std=c++11`

### Testing/Running
In the main folder, run the run.py script.
