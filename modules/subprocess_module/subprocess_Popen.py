#!/usr/bin/env python

from subprocess import call, check_call, check_output
from subprocess import run
from subprocess import Popen, PIPE

call(['ls', '-l', '/dev/null'])
lines = check_output(['ls', '-l', '/dev/null'], universal_newlines=True)
print(lines)

# process information is derived from Popen constructor
p = Popen(['python3', 'echo.py'], stdin=PIPE, stdout=PIPE, bufsize=0)
p.stdin.write(b'Hello\n')
p.stdin.flush()
p.stdout.flush()
p.stdout.readline()
p.stdout.flush()
