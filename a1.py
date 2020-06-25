Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #fibonacii series
number=int(input("enter the number"))
i=0
first=0
second=1
while(i<number):
            if(i<=1):
                      next=i
            else:
                  next=first+second
                  first=second
                  second=next
            print(next)
            i=i+1