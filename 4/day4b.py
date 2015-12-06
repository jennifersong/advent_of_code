import hashlib

# Now find one that starts with six zeroes.

key = 'ckczppom'

def find_adventcoin_hash(key):
  current_number = 0
  while hashlib.md5(key + str(current_number)).hexdigest()[0:6] != '000000':
    current_number += 1
  return current_number
  
print find_adventcoin_hash(key)