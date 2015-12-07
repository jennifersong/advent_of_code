import os
from collections import defaultdict

# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house),
# then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same
# script as the previous year.

def deliver_presents(location, directions):
  presents_delivered = defaultdict(int)
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
  return presents_delivered

starting_location = (0, 0)
with open(os.path.dirname(os.path.abspath(__file__)) + '/day3input.txt') as file:
  for line in file:
    # Because Santa and Robo-Santa alternate, divvy up directions by even/odd indices
    santa_presents = deliver_presents(starting_location, [direction for index, direction in enumerate(line) if index % 2 == 0])
    robo_presents = deliver_presents(starting_location, [direction for index, direction in enumerate(line) if index % 2 != 0])
    # Combine the two hashes into one to make sure we don't overcount
    total_presents = santa_presents.copy()
    total_presents.update(robo_presents)
  print len(total_presents.keys())