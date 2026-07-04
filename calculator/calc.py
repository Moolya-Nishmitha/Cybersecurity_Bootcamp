print("Simple Calculator <3 ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
choose = input("Choose operation (+, -, *, /): ")
if choose == "+":
    print(a+b)
elif choose == "-":
    print(a-b)
elif choose == "*":
    print(a*b)
elif choose == "/":
    if b == 0:
        print("invalid")
    else :
        print(a/b)
else:
    print("invalid input :( ")
