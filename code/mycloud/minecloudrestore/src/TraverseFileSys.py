#!/usr/bin/python
import os
import re
def index(directory):
    # like os.listdir, but traverses directory trees
    stack = [directory]
    files = []
    pattern=re.compile('.*~')
    while stack:
        directory = stack.pop()
        for file in os.listdir(directory):
			if re.search(pattern,os.path.splitext(file)[1]):
				continue
			if file not in ['conf','src','db']:
				fullname = os.path.join(directory, file)
				yield fullname
				if os.path.isdir(fullname) and not os.path.islink(fullname):
					stack.append(fullname)

if __name__ == "__main__":
   index('..')
