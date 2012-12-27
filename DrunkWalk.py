import random

def checkCords(Start, Stop, Cord):
  """ Checks if a given set of coordiantes are legal in a given grid."""

  Condition = [False, False]

  for i in xrange(2):
    if Cord[i] < Start and Cord[i] > Stop:
      Condition[i] = True

  return Condition

def walk(Start, Stop):
  """walk() does the calculation for the current position. Random reverses direction. Calls check to see if the drunk has crossed the walking grid."""

  # Current Coordinate.
  Cord = []
  Cord = [random.randint(Start, Stop), random.randint(Start, Stop)]

  # Directional increments. For a 2D plane.
  Increments = [[1, 0], [0, 1], [1, 1]]

  # The steps the drunk can take.
  Steps = 100
  while Steps > 0:

    print("(x, y) - (%s, %s) ") %(str(Cord[0]), str(Cord[1]))

    # Decide which direction the drunk moves.
    while True:

      # Which increment the drunk uses.
      Direction = random.randint(0, 2)

      # The drunk's orientation.
      ReverseDirection = random.randint(0, 1)
      if ReverseDirection == 1:
        Increments[Direction][0] *= -1
        Increments[Direction][1] *= -1

      # Perform Update
      Cord[0] += Increments[Direction][0]
      Cord[1] += Increments[Direction][1]

      Current = checkCords(0, 100, Cord)
      if not Current[0] and  not Current[1]:
        break;
      else:
        for i in xrange(2):
          if Current[i] == 1:
            if Cord[i] > Stop:
             Cord[i] -= Increments[Direction][i]
            else:
              Cord[i] += Increments[Direction][i]

    Steps -= 1


if __name__ == '__main__':
  walk(0, 100)
