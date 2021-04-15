import re

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Invalid file name")
    quit()
total = 0
for line in fh:
    x = re.findall('[0-9]+', line)
    print(x)
    if not x:
        continue
    else:
        for no in x:
            total = total + int(no)

print(total)
