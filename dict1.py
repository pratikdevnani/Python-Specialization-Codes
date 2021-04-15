fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Invalid file name")
    quit()

count = dict()
for line in fh:
    if not line.startswith("From "):
        continue
    else:
        line = line.rstrip()
        words = line.split()
        count[words[1]] = count.get(words[1], 0) + 1

max_count = None
max_email = None

for key,val in count.items():
    if max_count == None or val > max_count:
        max_count = val
        max_email = key

print(max_email, max_count)
