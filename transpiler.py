import os
import sys

inputfile = open(sys.argv[1], "r")
elsepycode = inputfile.readlines()
inputfile.close()

output = open(sys.argv[1] + ".py", "a")

inelse = False

def lengthofws(string):
	return len(string)-len(string.lstrip())


lastlength = 0

for line in elsepycode:
	line = line.rstrip()
	
	if ":" in line and not line.strip().startswith("else"):
		inelse = False
	
	if line.strip().startswith("else"):
		if lengthofws(line) > lastlength:
			inelse = False
		if line.strip().startswith("else:"):
			inelse = False
			output.write(line + "\n")
		else:
			if not inelse:
				output.write(line.replace("else", "if") + "\n")
				inelse = True
			else:
				output.write(line.replace("else", "elif") + "\n")
		lastlength = lengthofws(line)
			
	else:
		output.write(line + "\n")
