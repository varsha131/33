Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #binary to decimal
num=list(input("input binary number"))
value=0
for i in range(len(num)):
     digit=num.pop()
     if digit=='1':
                    value=value+pow(2,i)
print("decimal value of the number is",value)