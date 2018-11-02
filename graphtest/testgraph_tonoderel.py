import sys
from testgraph_compile import numericalId
def printNode(line):
	myid = numericalId(line[0])
	for i in line[1:]:
		print(myid, numericalId(i), sep="\t")
print("parent\tchild")
with open("graph_raw.txt", "r") as infile:
	for line in infile:
		line = line.strip().split(",")
		if len(line) == 0:
			continue
		printNode(line)
