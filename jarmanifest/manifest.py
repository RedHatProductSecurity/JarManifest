"""
Module to handle jar manifest files
"""
from jarmanifest import log, archives

logger = log.getLogger('util.manifest')
manifestkeys = None

def getManifestkeys():
	global manifestkeys
	if manifestkeys is None:
		logger.debug('Generating manifest keys')
		manifestkeys = list(map(str.lower, [
		'Name','Specification-Title','Specification-Vendor',
		'Specification-Version','Implementation-Title',
		'Implementation-Version','Implementation-Vendor',
		'Implementation-URL', 'Extension-Name', 'Comment']))
		manifestkeys = [i.replace('-','') for i in manifestkeys]
	return manifestkeys

# From: http://docs.oracle.com/javase/1.4.2/docs/guide/jar/jar.html#Notes on Manifest and Signature Files
# No line may be longer than 72 bytes (not characters), in its
# UTF8-encoded form. If a value would make the initial line longer
# than this, it should be continued on extra lines
# (each starting with a single SPACE).
def getAttributes(manifestFile):
	logger.debug('Parsing attributes from %s'%(manifestFile))
	manifestkeys = getManifestkeys()
	mf = open(manifestFile,'r',encoding='utf8')
	manifest = []
	current = {}
	lines = mf.readlines()
	idx = 0
	while idx<len(lines):
		line = lines[idx].strip()
		if len(line) > 0:
			splits = line.split(':')
			key = splits[0].lower().strip().replace('-','')
			if key in manifestkeys:
				value = ':'.join(splits[1:]).strip()
				current[key] = value
				while len(line.encode('utf-8')) >= 70:
					if idx<len(lines)-1:
						next_line = lines[idx+1]
						if next_line[0] == ' ':
							current[key] += next_line.strip()
							idx += 1
							line = next_line
							continue
					break
		elif len(current)>0 :
			count = len(current.values())
			# We need to weed out name only entries
			# We can manually interrogate packages
			if count > 1 or (count==1 and 'name' not in current.keys()):
				manifest.append(current)
			current = {}
		idx += 1
	if current != {}:
		manifest.append(current)
	return manifest
