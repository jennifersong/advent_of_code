import os
from collections import defaultdict

# Now, a nice string is one with all of the following properties:
#
# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

def check_nice_string(strng):
  one_repeat_between_flag = False
  letter_tracker = defaultdict(list)
  previous_letter = ''
  previous_two_letters = ['', '']
  
  for index, letter in enumerate(strng):
    # Check for pair of any two letters appearing twice in string without overlapping
    if previous_letter:
      # Track pairs of letters in hash: pairs are keys, indices of pairs are values
      # Get all noted locations for the current two-letter string
      previous_pairs = letter_tracker[previous_letter + letter]
      # If the second index of a pair location is equal to the current letter index - 1,
      # then those pairs are overlapping and we don't want to add it
      if all(pair[1] != index - 1 for pair in previous_pairs):
        letter_tracker[previous_letter + letter].append([index - 1, index])
    
    # Check for one letter that repeats with exactly one letter between its repeat
    if previous_two_letters[0] == letter and previous_two_letters[1]:
      one_repeat_between_flag = True
    
    # Update state-keeping variables  
    previous_letter = letter
    previous_two_letters.append(letter)
    previous_two_letters = previous_two_letters[1:]
  
  return one_repeat_between_flag and any(len(value) >= 2 for key, value in letter_tracker.items())
  
with open(os.path.dirname(os.path.abspath(__file__)) + '/day5input.txt') as file:
  file_characteristics = {True: 0, False: 0}
  for line in file:
    result = check_nice_string(line)
    file_characteristics[result] += 1
  print file_characteristics[True]