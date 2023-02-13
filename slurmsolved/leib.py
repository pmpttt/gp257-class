#!/usr/bin/env python3

LPi = 0
for i in range (999999):
    if i%2 == 1:
        LPi -= 4/(2*i+1)
    else:
        LPi += 4/(2*i+1)

res = str(LPi)

f=open("result0.txt","w")
f.write(res)
f.close()
