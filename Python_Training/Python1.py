a = int(input())

sum = 0

while(a>0):
   
  c=int(a/10)
 
  b=int(a%10)
  
  sum=sum+b
  
  a=c

print(int(sum))


