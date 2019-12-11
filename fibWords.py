import math
testcases=int(input()) 	
for t in range(0,testcases):
	a,b,n=input().split(' ')
	n=int(n)
	la=len(a)
	lb=len(b)
	lc=la+lb
	size=int(lc)
	prev=size
	A="a"
	B="b"
	C=A+B
	#print("current c ",lc, "and value is  : ",C)
	i=0
	while size<n:
		la=lb
		lb=lc
		lc=la+lb
		prev=size
		size=lc	
		i=i+1
		print("i : ",i,"and previous is ",prev," and size ",size)
# if n>prev:
# 	#something
# else:
# 	#Something
		






#print("c is : ",lc," size= ",size,"and value of c is ",C)
# 2,2,4,6,10,16
# 	59,67,###################################################################################5967,675967,5967675967,6759675967 675967	
# 	a=59
# 	b=67


# 	a,b,ab,bab,abbab,
# 	14th term

# 	begins with b and ends with b--even term
# 	begins with a and ends with b --odd term

# bababbab
# 2+2+2+2+2+2+2+2
# 6759675967675967

	