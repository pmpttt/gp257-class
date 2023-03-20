#!/usr/bin/env python3

import numpy as np
import mpi4py
from mpi4py import MPI
    
N = 40960
M = 64
dtype = np.float64
    
# Set up MPI, get rank and size, and define necessary variables
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
chunk_size = N // M
start = rank * chunk_size
end = start + chunk_size

# Generate random matrices A and B
if rank == 0:
    A = np.random.rand(N, N).astype(dtype)
    B = np.random.rand(N, N).astype(dtype, order='F')
    
comm.Barrier()

# Scatter chunks of A and B to all processes
local_A = np.zeros((chunk_size, N), dtype=dtype)
local_B = np.zeros((N, chunk_size), dtype=dtype, order='F')
if rank == 0:
    comm.Scatter(A[start:end, :], local_A, root=0)
    comm.Scatter(B[:, start:end], local_B, root=0)

comm.Barrier()
    
# Perform local matrix multiplication
local_C = np.zeros((chunk_size, chunk_size), dtype=dtype)
for i in range(chunk_size):
    for j in range(chunk_size):
        for k in range(N):
            local_C[i, j] += local_A[i, k] * local_B[k, j]

            
comm.Send(local_C,0)

# Combine results at rank 0
if rank == 0:
    result = np.zeros((N, N), dtype=dtype)
    for i in range(size):
        start = i * chunk_size
        end = start + chunk_size
        comm.Recv(result[start:end, :], source=i)
