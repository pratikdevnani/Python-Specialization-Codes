small = None
lar = -1
while True:
    num = input('enter a number:')
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print('Invalid input')
        continue
    if small is None:
        small = num
    elif num < small:
        small = num
    if num > lar:
        lar = num

print('Maximum is', lar)
print('Minimum is', small)
