import hashlib

# To do this, he needs to find MD5 hashes which, in hexadecimal,
# start with at least five zeroes. The input to the MD5 hash is
# some secret key (your puzzle input, given below) followed by a
# number in decimal. To mine AdventCoins, you must find Santa the
# lowest positive number (no leading zeroes: 1, 2, 3, ...) that
# produces such a hash.

key = 'ckczppom'

def find_adventcoin_hash(key):
  current_number = 0
  while hashlib.md5(key + str(current_number)).hexdigest()[0:5] != '00000':
    current_number += 1
  return current_number
  
print find_adventcoin_hash(key)