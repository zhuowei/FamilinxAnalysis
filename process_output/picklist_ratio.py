import sys
import random
rand = random.Random(1337)
with open(sys.argv[1], "r") as infile:
	alllines = infile.read().strip().split("\n")
alllines.sort(key=int)
print(alllines[0])
print(alllines[-1])
print(len(alllines))
subsetlines = rand.sample(alllines, int(len(alllines) * float(sys.argv[3])))
print(len(subsetlines))
# https://stackoverflow.com/questions/3426108/how-to-sort-a-list-numerically
subsetlines.sort(key=int)
with open(sys.argv[2], "w") as outfile:
	outfile.write("\n".join(subsetlines))
