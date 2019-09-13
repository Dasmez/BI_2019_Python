a = float(input())
operator = input()
b = float(input())
if operator =='+':
    print(a+b)
elif operator =='-':
    print(a-b)
elif operator =='*':
    print(a*b)
elif operator =='/':
    print(a/b)
else:
    print('unknown command')