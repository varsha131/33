Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #to count odd or even
numbers=(0,1,2,3,4,5,6,7,8,9,10)
count_odd=0
count_even=0
for x in numbers:
                  if not x%2:
                               count_even+=1
                  else:
                               count_odd+=1
print("even numbers",count_even)
print("odd numbers",count_odd)