import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src, "r")
tab = f.read()
f.close()

f = open(dst, "w")
f.write(tab.replace("\t", " "*2))
f.close()