def main():
    a = int(input("Lower Limit: "))
    b = int(input("Upper Limit: ")) + 1
    fizzbuzz(a,b)

def fizzbuzz(a,b):
    for i in range(a,b):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
            continue
        elif i%3==0:
            print("fizz")
            continue
        elif i%5==0:
            print("buzz")
            continue
        else:
            print(i)

main()