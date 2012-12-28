import random

def check_cords(start, stop, cord):
  """ Checks if a given set of coordiantes are legal in a given grid."""

  condition = [False, False]

  for i in xrange(2):
    if cord[i] < start or cord[i] > stop:
      condition[i] = True

  return condition

def walk(start, stop):
  """walk() does the calculation for the current position. Random reverses direction. Calls check to see if the drunk has crossed the walking grid."""

  # Current Coordinate.
  cord = []
  cord = [random.randint(start, stop), random.randint(start, stop)]

  # Directional increments. For a 2D plane.
  increments = [[1, 0], [0, 1], [1, 1]]

  # The steps the drunk can take.
  steps = 100
  while steps > 0:

    print("Step %d. (%s, %s) ") %(100 - steps, str(cord[0]), str(cord[1]))

    # Decide which direction the drunk moves.
    while True:

      # Which increment the drunk uses.
      direction = random.randint(0, 2)

      # The drunk's orientation.
      reverse_direction = random.randint(0, 1)
      if reverse_direction == 1:
        increments[direction][0] *= -1
        increments[direction][1] *= -1

      # Perform Update
      cord[0] += increments[direction][0]
      cord[1] += increments[direction][1]

      current = check_cords(0, 100, cord)
      if not current[0] and not current[1]:
        break;
      else:
        for i in xrange(2):
          if current[i] == 1:
            if cord[i] >= stop:
             cord[i] = cord[i] - 1
            elif cord[i] <= start:
             cord[i] += 1

    steps -= 1


if __name__ == '__main__':
  walk(0, 100)
