import os
import sys

inputfile = open(sys.argv[1], "r")

code = inputfile.readlines()
inputfile.close()

output = open(sys.argv[1] + ".py", "a")

inelse = False

def lengthofws(string):
	return len(string)-len(string.lstrip())


lastlength = 0

for line in code:
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
				output.write(line.replace("else", "if", 1) + "\n")
				inelse = True
			else:
				output.write(line.replace("else", "elif", 1) + "\n")
		lastlength = lengthofws(line)
	elif line.strip() == "INELSE0":
		inelse = False
	elif line.strip() == "INELSE1":
		inelse = True
	else:
		output.write(line + "\n")
