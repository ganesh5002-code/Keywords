#going through the loop till I find a letter a
x = str(input("Enter a word so that I can find an a:"))
for i in x:
    if (i=="a"):
        print("a is found")
        break
    else:
        print("a is not found")
    