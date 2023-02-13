#!/user/bin/env python3

import random
import os

# Get task ID and set as seed
taskID = os.getenv('SLURM_ARRAY_TASK_ID')
random.seed(taskID)

# Initialize variable of sums that are less than or equal to 1
lteq = 0

# Loop 100000 times and write number of random combinations that sum to less than or equal to 1
for i in range (99999):
    first = random.random()
    second = random.random()
    if (first**2 + second**2) <= 1:
        lteq += 1
        
est = 4*(lteq/100000)
res = str(est)

fname = "piest" + str(taskID)

f = open(fname,"w")
f.write(res)
f.close()
    
