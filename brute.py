from mpi4py import MPI
import sys
import hashlib
from BruteClass import BruteForce

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def list_split(lst, n):
    return [ lst[i::n] for i in xrange(n) ]

hash_str = str(sys.argv[1]).lower()
length = int(sys.argv[3])

dictionary = {
	'1': '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
	'2': '0123456789',
	'3': 'abcdefghijklmnopqrstuvwxyz',
	'4': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
	'5': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
	'6': '0123456789abcdefghijklmnopqrstuvwxyz',
	'7': '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
}
dict_list = dictionary[sys.argv[2]] if sys.argv[2] in dictionary else ''
first_letters = list_split(dict_list, size)

brute = BruteForce(hash_str, length, first_letters[rank], dict_list)
#print 'Proces:', rank, 'z zestawem liter: [', first_letters[rank], ']'
password = brute.password()
if password != -1:
	print password