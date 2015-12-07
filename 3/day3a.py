import os
from collections import defaultdict

# Santa is delivering presents to an infinite two-dimensional grid of houses.
#
# He begins by delivering a present to the house at his starting location, and then an
# elf at the North Pole calls him via radio and tells him where to move next. Moves are
# always exactly one house to the north (^), south (v), east (>), or west (<). After each
# move, he delivers another present to the house at his new location.

# Location notation doesn't really matter as long as you are consistent about how
# you traverse according to the directions, but we'll start with (0, 0) and modify the
# y-coordinate when going up and down and the x-coordinate when going right and left
def deliver_presents(location, directions):
  presents_delivered = defaultdict(int)
  # Deliver a present to the starting location
  presents_delivered[location] += 1
  for direction in directions:
    if direction == '^':
      location = (location[0], location[1] + 1)
    elif direction == 'v':
      location = (location[0], location[1] - 1)
    elif direction == '>':
      location = (location[0] + 1, location[1])
    elif direction == '<':
      location = (location[0] - 1, location[1])
    presents_delivered[location] += 1
  # Return a hash of {location: num_presents_delivered}
  return presents_delivered

starting_location = (0, 0)
with open(os.path.dirname(os.path.abspath(__file__)) + '/day3input.txt') as file:
  for line in file:
    total_presents = deliver_presents(starting_location, line)
  print len(total_presents.keys())