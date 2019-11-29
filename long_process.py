MAX=10**8
for i in range(MAX+1):
    if i%10**7==0:
        print(' %.0f%%'% (i/MAX*100))
