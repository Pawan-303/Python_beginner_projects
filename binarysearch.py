import time


def bsearch(ls,low,high,t):
    while(low<=high):
        mid=int((low +high)//2)
        if ls[mid]==t:
            return mid
        elif t>ls[mid]:
            low=mid+1
        else:
            high=mid-1
    else:
        return -1
    

def naive_search(l,low,t):
    if l[low]==t:
        return low
    else:
        if low==len(l)-1:
            return -1
        else:return naive_search(l,low+1,t)


l=list(map(int,input('Enter the numbers in list ,space saperated \n').split()))
t=int(input("Enter the no to search\n"))
print('befor sort : ',l)
l.sort()
print('After sort : ',l)
low=0
high=len(l)-1

start=time.time()
result=bsearch(l,low,high,t)
end=time.time()
if result!=-1:
    print('The target no is found at index {}'.format(result))
    print(f'time taken in binary search: {end-start} seconds')
else:
    print('no not found')


start=time.time()
result1=naive_search(l,low,t)
end=time.time()
if result!=-1:
    print('The target no is found at index {}'.format(result1))
    print(f'time taken in naive search : {end-start}')
else:
    print('no not found')

