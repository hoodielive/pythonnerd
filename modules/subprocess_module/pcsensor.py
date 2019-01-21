#!/usr/bin/env python

import re
from subprocess import *

try:
    # Execute process
    output = Popen(['ls', '-tlr'], stdout=PIPE).communicate()[0]
    print(ouput)

    # Parse Results with Regex
    p = re.compile(r'\s+')
    s = p.split(output)
    s.pop()
    print(s)

    # Assign Interesting Elements to new VARs
    d = s[0]
    t = s[1]
    tem = s[3]

    # Strip trailing temp value (F|C)
    tem2 = tem[:-1]
    print("DATE: ", d, " Time:", t, "TEMPERATURE: ", tem2)

except OSError as err1:
    print("ERROR: ", err1)
    exit(200)
