count = int(input("Enter a positive integer: "))
i = 0
n1 = 0
n2 = 1

if (count <= 0):
    print("Must be a positive integer!")
else:
    print("Fibonacci sequence: ")
    while i < count:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        i += 1