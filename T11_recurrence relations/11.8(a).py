#s0=0
#s1=1          = s0+a1
#s2= 1-2=-1    = s1-2= s1+a2
#s3= 1-2+3=2   = s3+3= s2+a3
#s4= 1-2+3-4= -2  = s4-4 = s3+a4
#sn= s(n-1)+(-1)^n*n = s(n-1)+an
#a0=1
#a1=1
#a2=-2
#a3=3
#a4=-4
#an= (-1)^n*n
#an= a(n-1)* (-1)^n*n
def b(n):
    s0=0
    a0=0
    for i in range (1, n+1):
        a0 = a0 * ((-1)**(i))*i
        s0= s0+a0
    return s0
n=10
for i in range (n):
    print(b(i), end= " ")
print()