# mpi-intro

Code for exercises in this MPI tutorial https://pdc-support.github.io/introduction-to-mpi/.

Note that there are bugs in the tutorial in the provided solutions for - 
- Pingpong exercise in [Module 3 MPI Send and Recv](https://pdc-support.github.io/introduction-to-mpi/03-mpi_send_recv/index.html). 
The code hangs when run with a big enough send message buffer because of an unmatched `send` call in one of the two processes.
- Last exercise in [Module 6 Non-Blocking Communication](https://pdc-support.github.io/introduction-to-mpi/06-nonblocking/index.html). 
Here we get a seg fault when run with a big enough send message buffer. Possibly related to [this issue](https://stackoverflow.com/questions/59559597/mpi4py-irecv-causes-segmentation-fault).

Python scripts can be run using `mpirun -n n_processes python script.py`.
