def fibonacci(N):
    a=0
    b=1
    i=0
    while i!=N:
        a,b=b,a+b
        
        print(i+1,"\t\t",a)
        i+=1
N=int(input("Enter a Value:"))
print("SL NO.","\t","Fibonacci Value")
fibonacci(N)