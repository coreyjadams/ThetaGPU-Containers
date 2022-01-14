from mpi4py import MPI
import mpi4py;
print(mpi4py.__file__)
print(MPI.COMM_WORLD.Get_rank())
