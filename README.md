# python-programs
def add(a,b): 
    return a+b 
def sum(a,b): 
    return a-b 
def mul(a,b): 
    return a*b 
def div(a,b): 
    return a/b 
a=int(input("enter a val: ")) 
o=input("Enter operator: ") 
b=int(input("Enter b value: ")) 
if o=="+": 
    print(add(a,b)) 
elif o=="-": 
    print(sub(a,b)) 
elif o=="*": 
    print(mul(a,b)) 
elif o=="/": 
    print(div(a,b)) 
else: 
    print("Enter correct operator.") 
 
