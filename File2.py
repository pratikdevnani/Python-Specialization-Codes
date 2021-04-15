fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Invalid file name")
    quit()

total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        line = line.rstrip()
        line = line.replace(" ","")
        ind = line.find(':')
        total = total + float(line[ind+1:])
        count = count + 1

print('Average spam confidence:', total/count)
