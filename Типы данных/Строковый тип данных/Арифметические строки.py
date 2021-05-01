a = input()
b = input()
c = input()
#if len(max(a,b,c,key=len))-len(min(a,b,c,key=len))==len(a)+len(b)+len(c)-len(max(a,b,c,key=len))-len(min(a,b,c,key=len)):
#    print('YES')
#else:
#    print('NO')

#print(len(a)+len(b)+len(c)-len(max(a,b,c,key=len))-len(min(a,b,c,key=len)))
#print((len(max(a,b,c,key=len))-len(min(a,b,c,key=len)))/2)
if len(a)+len(b)+len(c)-len(max(a,b,c,key=len))-len(min(a,b,c,key=len))==(len(max(a,b,c,key=len))+len(min(a,b,c,key=len)))/2:
    print('YES')
else:
    print('NO')