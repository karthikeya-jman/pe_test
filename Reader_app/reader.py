f = open("/shared/counter.txt","r")
count = int(f.read())
print("reading",count)