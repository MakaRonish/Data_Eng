lst = [i for i in range(1, 11) if i % 3 == 0]
print(lst)

def isPrime(x):
    for i in range(2,int(x/2)+1):
        if x%i==0:
            return False
    return True

my_lst=[i for i in range(1,101) if isPrime(i)]
print(my_lst)
