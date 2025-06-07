n = int(input("Enter a number of fibonacci terms:"))

fibo_seq = []

a,b=0,1

for _ in range(n):
    fibo_seq.append(a)
    a,b=b,a+b

print(f"fibonacci sequnce for",n,"is",fibo_seq) 