f = open("/shared/counter.txt","r")
count = int(f.read())
with open('/shared/counter.txt', 'w') as file:
    print("before write",count)
    file.write(str(count+1))