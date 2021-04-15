fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Invalid file name")
    quit()

time_dict = dict()
for line in fh:
    if not line.startswith("From "):
        continue
    else:
        line = line.rstrip()
        words = line.split()
        time = words[5].split(':')
        time_dict[time[0]] = time_dict.get(time[0], 0) + 1

l = sorted((k,v) for k,v in time_dict.items())
for k,v in l:
    print(k,v)
