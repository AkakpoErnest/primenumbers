number = int(input("Enter number"))
if number > 1:
    for num in range(2,number):
        if (number  % num) == 0:
            print (number," is not a prime number")
            break
        elif number == 1:
            print("it is not  a prime number")
        else:
            print(number,"is  a prime number")
            break
