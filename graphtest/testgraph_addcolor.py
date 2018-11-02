import sys
with open(sys.argv[1], "r") as infile:
	indot = infile.read().strip().rstrip("}")
	print(indot)
with open(sys.argv[2], "r") as outfile:
	for l in outfile:
		l = l.strip()
		if l == "":
			continue
		print(l, "[style=filled fillcolor=\"#A5D6A7\"]")
print("}")
	
