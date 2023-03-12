from mpi4py import MPI

# rank = MPI.COMM_WORLD.Get_rank()
# print(f"My rank is {rank}")

# n_ranks = MPI.COMM_WORLD.Get_size()
# print(f"From rank[{rank}]: world size is {n_ranks}")

# Exercises

# Q1 - Hello world
# print("Hello world!")

# rank = MPI.COMM_WORLD.Get_rank()
# print(f"My rank is {rank}")

# n_ranks = MPI.COMM_WORLD.Get_size()
# print(f"From rank[{rank}]: world size is {n_ranks}")

# Q2 - Using the ranks
# a, b = 1, 2
# rank = MPI.COMM_WORLD.Get_rank()
# if rank == 0:
#     print(f"from rank[{rank}]: {a - b}")
# elif rank == 1:
#     print(f"from rank[{rank}]: {a + b}")
# elif rank == 2:
#     print(f"from rank[{rank}]: {a * b}")

# Q3 - Parallel loop
numbers = 10
rank = MPI.COMM_WORLD.Get_rank()
n_ranks = MPI.COMM_WORLD.Get_size()

numbers_per_rank = numbers // n_ranks

if numbers % n_ranks > 0:
    numbers_per_rank += 1

my_first = rank * numbers_per_rank
my_last = my_first + numbers_per_rank

for i in range(my_first, my_last):
    if i < numbers:
        print(f"rank[{rank}] printing number {i}")
