for i in range(31):
    if i % 20==0:
        print("Twist")
    elif i % 15==0:
        pass
    elif i % 5==0:
        print("Fizz")
    elif i % 3==0:
        print("buzz")
    else:
        print(i)