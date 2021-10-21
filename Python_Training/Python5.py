entry=0
sum=0
while True:
  entry = int(input())
  if entry<0:
    continue
  sum+=entry
print(sum)