# Program to Check Prime Number, use for loop.
number = int(input("Enter a number: "))

if number <= 1:
    print("Not prime")
else:
    for i in range(2, number):
        if number % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")