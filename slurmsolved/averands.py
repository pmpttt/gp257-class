#!/usr/bin/env python3

import os

# Initialize count and sum variables
count = 0
sumpis = 0

# Loop over items in directory to find estimates, add to sum, and iterate count
with os.scandir() as entries:
    for entry in entries:
        if "piest" in entry.name:
            f = open(entry.name)
            count += 1
            sumpis += float(f.read())
            f.close()
            os.remove(entry.name)

piestave = sumpis/count
res = str(piestave)

f = open("result2","w")
f.write(res)
f.close()
