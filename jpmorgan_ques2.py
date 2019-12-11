import itertools
def findsubsets(s, n): 
    return [set(i) for i in itertools.combinations(s, n)] 

test=int(input())

for i in range(test):
    n=int(input())
    k=int(input())
    l=input().split(' ')
    array = [int(i) for i in l]
    subsets=findsubsets(array, n)
    for subset in subsets:
        

