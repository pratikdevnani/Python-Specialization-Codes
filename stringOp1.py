text = "X-DSPAM-Confidence:    0.8475";
loc = text.find("0")
num = text[loc:]
num = float(num)
print(num)
