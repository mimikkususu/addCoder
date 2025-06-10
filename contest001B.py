num  = int(input())/1000

if num < 0.1:
    VV = "00"
elif 0.1 <= num <=5:
    VV = int(num*10)
    if VV < 10:
        VV = "0"+str(int(num*10))
elif 6 <= num <= 30:
    VV = num + 50
elif 35 <= num <= 70:
    VV = (num - 30)/5 + 80
elif 70 < num:
    VV = 89

if type(VV) == str:
    print(VV)
else:
    print(int(VV))
