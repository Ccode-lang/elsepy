import os
import sys

inputfile = open(sys.argv[1], "r")
elsepycode = inputfile.readlines()
inputfile.close()

output = open(sys.argv[1] + ".py", "a")

inelse = False

for line in elsepycode:
	line = line.rstrip()
	if line.strip().startswith("else"):
		if line.strip().startswith("else:"):
			inelse = False
			output.write(line + "\n")
		else:
			if not inelse:
				output.write(line.replace("else", "if") + "\n")
				inelse = True
			else:
				output.write(line.replace("else", "elif") + "\n")
			
	else:
		output.write(line + "\n")
