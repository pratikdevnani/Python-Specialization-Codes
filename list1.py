fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Invalid file name")
    quit()

lst = list()
for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
