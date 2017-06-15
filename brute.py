from mpi4py import MPI
import sys
import hashlib
from BruteClass import BruteForce

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def list_split(lst,n):
    return [ lst[i::n] for i in xrange(n) ]

hash_str = str(sys.argv[1]).lower()
length = int(sys.argv[3])

if (int(sys.argv[2]) == 1):
    dict_list = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
elif (int(sys.argv[2]) == 2):
    dict_list = '0123456789'
elif (int(sys.argv[2]) == 3):
    dict_list = 'abcdefghijklmnopqrstuvwxyz'
elif (int(sys.argv[2]) == 4):
    dict_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
elif (int(sys.argv[2]) == 5):
    dict_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
elif (int(sys.argv[2]) == 6):
    dict_list = '0123456789abcdefghijklmnopqrstuvwxyz'
elif (int(sys.argv[2]) == 7):
    dict_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
else :
    dict_list = ''

first_letters = list_split(dict_list, size)

brute = BruteForce(hash_str, length, first_letters[rank], dict_list)
#print 'Proces:', rank, 'z zestawem liter: [', first_letters[rank], ']'
password = brute.password()
if password != -1:
	print password