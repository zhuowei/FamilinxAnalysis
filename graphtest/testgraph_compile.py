globalCounter = 1
globalMap = {}
numericalOnly = False

def numericalId(nodename):
	global globalCounter
	if not nodename in globalMap:
		globalMap[nodename] = globalCounter
		globalCounter += 1
	return globalMap[nodename]
def nodeSlug(nodename):
	if numericalOnly:
		return str(numericalId(nodename))
	return nodename + "_" + str(numericalId(nodename))
