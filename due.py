def change(a,b):
    if a>b:
        return a-b
    elif b>a:
        return b-a
    else:
        return "There is no change"
a = 2.50
b = 4
print("The cost is $", a)
print("The payment is $", b)
print("The change the buyer gets is $", change(a,b))