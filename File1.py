fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Invalid File name")
    quit()

for line in fh:
    line = line.rstrip()
    print(line.upper())
    
