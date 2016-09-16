import re

# file foo = open("kill.pcapng", "r")
pattern = 'flag\{.*\}'
for i, line in enumerate(open('kill.pcapng')):
    for match in re.finditer(pattern, line):
        print 'Found on line %s: %s' % (i+1, match.group(0))
