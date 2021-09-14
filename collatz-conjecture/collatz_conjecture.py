def steps(n):
    if(n<=0):
        raise ValueError ("n must be positive")
    else:
        s=0
        while(n>1) :
            s=s+1
            # if n is odd:
            if (n % 2) != 0:
                n = 3*n + 1
            # else n is even:
            else:
                n = n/2
        return(s)

#n = int(input('Enter n: '))
#print('Number of steps: ', end=steps(n))
#steps(n)



