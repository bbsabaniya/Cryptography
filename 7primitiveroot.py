import sys

def getG(p):
    r = set(range(1, p))
    res = []
    for i in r:
        gen = set()
        for x in r:
            gen.add(pow(i,x,p))
        if gen == r:
            res.append(i)
            if (len(res)>10): break
    return res

p=7

if (len(sys.argv)>1):
 p=int(sys.argv[1])

print("Computing the first 10 generators")

g=getG(p)
print(f"p={p}")
print(f"g={g}")


print(f"\nNow trying the first 20 values for {g[0]} (there should be no repeated values):")
print(f"x\tg^x (mod p)")
print(f"===================")
for i in range(0,p):
	print(f"{i}\t{pow(g[0],i,p)}")
	if (i>20): break
