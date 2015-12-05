import os

# A nice string is one with all of the following properties:
#
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

vowels = 'aeiou'
forbidden_strings = ['ab', 'cd', 'pq', 'xy']

def check_nice_string(strng):
  num_vowels = 0
  double_letter_flag = False
  previous_letter = ''
  for letter in strng:
    if letter in vowels:
      num_vowels += 1
    if not(double_letter_flag) and previous_letter == letter:
      double_letter_flag = True
    if previous_letter + letter in forbidden_strings:
      return False
    previous_letter = letter
  return num_vowels >= 3 and double_letter_flag
  
with open(os.path.dirname(os.path.abspath(__file__)) + '/day5input.txt') as file:
  file_characteristics = {True: 0, False: 0}
  for line in file:
    result = check_nice_string(line)
    file_characteristics[result] += 1
  print file_characteristics[True]
