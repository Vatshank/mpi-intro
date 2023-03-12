from mpi4py import MPI

rank = MPI.COMM_WORLD.Get_rank()
n_ranks = MPI.COMM_WORLD.Get_size()

# Example 1 - sending and receiving 

# s_message = "yaba daabaaa doooo"
# r_message = MPI.COMM_WORLD.gather(s_message, root=0)

# if rank == 0:
#     for i in range(n_ranks):
#         print(r_message[i])

# Example 2 - Reductions
comm = MPI.COMM_WORLD
n_nums = 1024
first_n = n_nums * rank
vector = list(range(first_n, first_n + n_nums))

my_sum = sum(vector)
my_max = max(vector)

global_sum = comm.allreduce(my_sum, op=MPI.SUM)
global_max = comm.allreduce(my_max, op=MPI.MAX)

print(global_sum, global_max)
