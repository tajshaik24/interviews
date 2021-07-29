import sys
from collections import defaultdict

# Prints to standard output.
def findStartAndEndLocations(pairs):
  # Initialization of Variables
  inputs, outputs = [], set()
  inputOutputMapping = defaultdict(list)
  returnPairing = defaultdict(set)

  # Adding Values to Data Structures
  for p in pairs:
    if p[0] not in inputs:
      inputs.insert(0, p[0])
    outputs.add(p[1])
    inputOutputMapping[p[0]].append(p[1])

  # Determining intersection btwn inputs and outputs
  intersection = list(set(inputs) & outputs)

  # Creating Stack for DFS
  inputs = [(i,i) for i in inputs if i not in intersection]

  # Running the DFS Algorithm
  while inputs:
    startVal, currNode = inputs.pop()
    if currNode not in inputOutputMapping.keys():
      returnPairing[startVal].add(currNode)
    else:
      for elem in inputOutputMapping[currNode]:
        inputs.append((startVal, elem))

  # Formatting for STDOUT
  listSortedKeys = sorted(returnPairing.keys())
  for key in listSortedKeys:
    initString = ""
    valuesList = sorted(list(returnPairing[key]))
    for index in range(len(valuesList) - 1):
      initString += valuesList[index] + " "
    initString += valuesList[len(valuesList) - 1]
    print(key + ": " + initString)

# DO NOT MODIFY BELOW THIS LINE
def main():
  pairs = []

  for line in sys.stdin:
    if len(line.strip()) == 0:
      continue

    line = line.rstrip()

    pairs.append(line.split(" "))

  findStartAndEndLocations(pairs)

main()
