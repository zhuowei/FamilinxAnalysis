import sys
def readsegment(infile):
	infile.readline()
	infile.readline()
	retval = infile.readline()
	infile.readline()
	infile.readline()
	return retval.strip();
def countperyear(infile, startyear=1800):
	year = startyear
	while True:
		total = readsegment(infile)
		male = readsegment(infile)
		female = readsegment(infile)
		if len(total) == 0 or len(male) == 0 or len(female) == 0:
			break
		yield (year, total, male, female)
		year += 1
def countperyearonlytotal(infile, startyear=1800):
	year = startyear
	while True:
		total = readsegment(infile)
		if len(total) == 0:
			break
		yield (year, total)
		year += 1

# file loading functions

# returns only the y values
def bfsout_output(filename):
	with open(filename, "r") as infile:
		return [int(a[1]) for a in countperyearonlytotal(infile)]
# returns (xvalues, total, male, female)
def fullcount_output(filename1, filename2):
	with open(filename1, "r") as infile1, open(filename2, "r") as infile2:
		# keep the 1800-1900 section of the first file, and append the second file afterwards
		allvals = list(countperyear(infile1, 1800))[1800-1800:1900-1800] + list(countperyear(infile2, 1900))
	xvalues = [int(a[0]) for a in allvals]
	total = [int(a[1]) for a in allvals]
	male = [int(a[2]) for a in allvals]
	female = [int(a[3]) for a in allvals]
	return (xvalues, total, male, female)

def main():
	startyear = int(sys.argv[2]) if len(sys.argv) >= 3 else 1800
	c = countperyear
	if len(sys.argv) >= 4 and sys.argv[3] == "True":
		c = countperyearonlytotal
	with open(sys.argv[1], "r") as infile:
		for t in c(infile, startyear):
			print(*t)
if __name__ == "__main__":
	main()
