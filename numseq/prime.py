def is_prime(m):
    if (m==1):
        return False
    elif (m==2):
        return True;
    else:
        for x in range(2,m):
            if(m % x==0):
                return False
        return True  

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]           
