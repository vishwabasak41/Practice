'''
# Sample code to perform I/O:
name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
a,b=input().split(' ')
a=int(a)
b=int(b)
result=-1
if a<b:
    small=a
    big=b
else:
    small=b
    big=a
for i in range(2,small+1):
    if small%i==0:
        if big%i==0:
            result=i
            break
print(result)
            
        