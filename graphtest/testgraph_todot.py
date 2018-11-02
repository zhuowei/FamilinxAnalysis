import sys
from testgraph_compile import nodeSlug
import testgraph_compile

def printGraphvis(line):
	print(nodeSlug(line[0]), "-> {", ",".join(nodeSlug(i) for i in line[1:]), "}")

if len(sys.argv) > 1 and sys.argv[1] == "num":
	testgraph_compile.numericalOnly = True

print("digraph {")

with open("graph_raw.txt", "r") as infile:
	for line in infile:
		line = line.strip().split(",")
		if len(line) == 0:
			continue
		printGraphvis(line)
print("}")
