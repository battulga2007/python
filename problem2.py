def input_number():
    number = int(input("add number: "))
    divisor = range(1, number+1)
    return number, divisor


def divisor_finder(number, divisor):
    x = []
    for i in divisor:
        if number % i == 0:
            x.append(i)
    return x


def main():
    number, divisor = input_number()
    x = divisor_finder(number, divisor)
    print("There is " + str(list(x)) + " divisors in the number " + str(number))


main()
