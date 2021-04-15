fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Invalid file name")
    quit()

count = 0
for line in fh:
    if not line.startswith("From"):
        continue
    elif not line.startswith("From:"):
        line = line.rstrip()
        words = line.split()
        count = count + 1
        print(words[1])

print("There were", count, "lines in the file with From as the first word")
