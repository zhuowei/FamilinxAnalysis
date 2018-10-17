import sys
def readsegment(infile):
	infile.readline()
	infile.readline()
	retval = infile.readline()
	infile.readline()
	infile.readline()
	return retval.strip();
with open(sys.argv[1], "r") as infile:
	year = 1800
	while True:
		total = readsegment(infile)
		male = readsegment(infile)
		female = readsegment(infile)
		if len(total) == 0 or len(male) == 0 or len(female) == 0:
			break
		print(year, total, male, female)
		year += 1
