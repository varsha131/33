Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #gcd of two numbers
def hcf(x,y):
              if x>y:
                      smaller=y
              else:
                      smaller=x
              for i in range(1,smaller+1): 
                                           if((x%i==0) and (y%i==0)):
                                                                      hcf=i
              return hcf
num1=54
num2=24
print(hcf(num1,num2))