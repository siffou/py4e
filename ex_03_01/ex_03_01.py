hours = input("Enter Hours:")
rate = input("Enter Rate:")
fh = float(hours)
fr = float(rate)

if fh > 40 :
    #print("Overtime")
    reg = fr * fh
    otp = (fh - 40) * (fr * 0.5)
    #print(reg, otp)
    xp = reg + otp
else:
    #print("Normal Hours")
    xp = fh * fr
print("Pay:", xp)
