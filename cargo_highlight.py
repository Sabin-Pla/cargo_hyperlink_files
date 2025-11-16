#!/bin/python
import re
import os
import subprocess
import codecs
from sys import argv

a = argv[1:]
sp = subprocess.run(["cargo", "--color=always", *argv[1:]], capture_output=True)

def escape_file_url(f):
	link=f"{f}"
	return f'\\033]8;;{link}\\033\\\\{f}\\033]8;;\\033\\'

s = sp.stderr
file_starter=r'(b\'\\x1b\[0m\s+\\x1b\[0m\\x1b\[0m\\x1b\[1m\\x1b\[38;5;12m-->\s+\\x1b\[0m\\x1b\[0m)(.+)\/([^\/]+):([0-9]+):([0-9]+)(\\x1b\[0m\'.*)'
print(file_starter)
possible_unmatched = []
for line in s.decode("ascii").splitlines():
	m = re.match(file_starter, str(line.encode()))
	if m:
		file = m.group(2) + '/' + m.group(3) + ":" + m.group(4)
		new_line = m.group(1) + escape_file_url(file) + ":" + "".join(m.group(5,6))
		new_line = codecs.decode(new_line[2:-1], "unicode_escape").encode("latin1")
		print(new_line.decode("ascii"))
	elif '-->' in line:
		possible_unmatched.append( str(line.encode()))
	else:
		print(line)
if len(possible_unmatched) >= 1:
	print(possible_unmatched)
	print("Possible unmatched files^")
