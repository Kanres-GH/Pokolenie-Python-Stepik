a = int(input())
print(a)                                #123
print(a//100, a%10, (a//10)%10, sep='') #132
print((a//10)%10, a//100, a%10, sep='') #213
print((a//10)%10, a%10, a//100, sep='') #231
print(a%10, a//100, (a//10)%10, sep='') #312
print(a%10, (a//10)%10, a//100, sep='') #321