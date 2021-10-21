word=input('Enter text')
vowel_count=0
for s in word:
  if s=='A' or s=='a' or s=='E' or s=='e' or s=='I' or s=='i' or s=='O' or s=='o' or s=='U' or s=='u':
    vowel_count+=1
print(vowel_count)     