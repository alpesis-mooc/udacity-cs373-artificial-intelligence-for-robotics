#Write code that outputs p after multiplying each entry 
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses.


p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

#Enter code here
p[0] = p[0] * pHit
p[1] = p[1] * pMiss
p[2] = p[2] * pMiss
p[3] = p[3] * pHit
p[4] = p[4] * pHit

print sum(p)
