from mpi4py import MPI
import sys

# Exercise 1 - Many ranks
# n_ranks = MPI.COMM_WORLD.Get_size()
# if n_ranks % 2:
#     print("Need even number of ranks! Bye bye.")
#     sys.exit(1)

# rank = MPI.COMM_WORLD.Get_rank()
# if rank % 2 == 0:
#     message = "Yaba daba doooo"
#     MPI.COMM_WORLD.send(message, dest=rank + 1, tag=0)
#     print(f"Sent message from rank[{rank}]")

# if rank % 2 == 1:
#     message = MPI.COMM_WORLD.recv(source=rank - 1, tag=0)
#     print(message)

# Exercise 2 - Hello again, world
# rank = MPI.COMM_WORLD.Get_rank()
# n_ranks = MPI.COMM_WORLD.Get_size()

# if rank > 0:
#     message = f"Yaba daba doooo from rank[{rank}]"
#     MPI.COMM_WORLD.send(message, dest=0, tag=0)
# if rank == 0:
#     for i in range(1, n_ranks):
#         message = MPI.COMM_WORLD.recv(source=i, tag=0)
#         print(message)

# Ecercise 3
# n_numbers = 10000

# # Get my rank and the number of ranks
# rank = MPI.COMM_WORLD.Get_rank()
# n_ranks = MPI.COMM_WORLD.Get_size()

# # Check that there are exactly two ranks
# if n_ranks != 2:
#     print("This example requires exactly two ranks")
#     sys.exit(1)

# # Call the other rank the neighbour
# if rank == 0:
#     neighbour = 1
# else:
#     neighbour = 0

# # Generate numbers to send
# send_message = []
# for i in range(n_numbers):
#     send_message.append(i)

# if rank == 0:
#     # Rank 0 will send first
#     MPI.COMM_WORLD.send(send_message, dest=1, tag=0)

#     # And rank 0 will receive the message
#     recv_message = MPI.COMM_WORLD.recv(source=1, tag=0)
#     print("Message received by rank", rank)

# if rank == 1:
#     # Rank 1 will receive it's message before sending
#     recv_message = MPI.COMM_WORLD.recv(source=0, tag=0)
#     print("Message received by rank", rank)

#     # Now rank 1 is free to send
#     MPI.COMM_WORLD.send(send_message, dest=0, tag=0)

# Exercise 4 - Ping Pong
max_count = 100
# ball = 1 # A dummy message to simulate the ball
ball = list(range(10000)) # TODO: this fails (hangs) with a big enough message size (works for the int ball above)

# Get my rank
rank = MPI.COMM_WORLD.Get_rank()

# Call the other rank the neighbour
if rank == 0:
    neighbour = 1
else:
    neighbour = 0

if rank == 0:
   # Rank 0 starts with the ball. Send it to rank 1
   MPI.COMM_WORLD.send(ball, dest=1, tag=0)

# Now run a send and receive in a loop untill someone gets bored
counter = 0
bored = False
while not bored:
   # Receive the ball
   ball = MPI.COMM_WORLD.recv(source=neighbour, tag=0)

   # Increment the counter and send the ball back
   counter += 1
   MPI.COMM_WORLD.send(ball, dest=neighbour, tag=0)

   # Check if the rank is bored
   bored = (counter >= max_count)

print("Rank {:d} is bored and giving up".format(rank))

# Random
# rank = MPI.COMM_WORLD.Get_rank()
# n_numbers = 10000
# send_message = []
# for i in range(n_numbers):
#     send_message.append(i)
# MPI.COMM_WORLD.send(send_message, dest=1 - rank, tag=0)
# msg = MPI.COMM_WORLD.recv(source=1 - rank, tag=0)
# print("Message received by rank", rank)