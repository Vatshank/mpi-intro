from mpi4py import MPI
import sys

rank = MPI.COMM_WORLD.Get_rank()
n_ranks = MPI.COMM_WORLD.Get_size()

if n_ranks < 2:
    print("This example requires at least two ranks")
    sys.exit(1)

# if rank == 0:
#     message = "yaba daabaa doooo"
#     req = MPI.COMM_WORLD.isend(message, dest=1, tag=0)

# if rank == 1:
#     req = MPI.COMM_WORLD.irecv(source=0, tag=0)
#     message = req.wait()
#     print(req)

# Example 1 - Non Blocking Comm
# TODO: bug (seg fault) - doesn't work for size 100000 but works for 10000
# send_message = list(range(10000))
send_message = list(range(100000))
neighbor = 1 - rank

# Send the message to other rank
s_req = MPI.COMM_WORLD.isend(send_message, dest=neighbor, tag=0)

# Receive the message from the other rank
r_req = MPI.COMM_WORLD.irecv(source=neighbor, tag=0)

recv_message = r_req.wait()
print("Message received by rank", rank)
