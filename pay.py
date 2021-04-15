def computepay(h,r):
    if h <= 40:
        p = h*r
    else:
        p = (40*r) + (h-40)*(1.5*r)
    return p
try:
  hrs = float(input("Enter Hours:"))
  rate = float(input("Enter rate:"))
except:
  print("The input value is not a number")
  quit()
p = computepay(hrs,rate)
print("Pay",p)
