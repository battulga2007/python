def summ(numbers):
    total = 0
    for i in numbers:
        total += i

    return total

def avg(numbers):
    added_up = summ(numbers)
    average = added_up/len(numbers)
    print("The sum is", added_up)
    print("The average is", average)

def maximum_minimum(numbers):
    sorted_max = 0
    sorted_min = numbers[0]

    for i in numbers:
        if i > sorted_max:
            sorted_max = i

    for i in numbers:
        if i < sorted_min:
            sorted_min = i

    print("The maximum is", sorted_max)
    print("The minimum is", sorted_min)

def count_even_odd(numbers):
    even = 0
    odd = 0

    for i in numbers:
        if i == 0:
            continue
        elif i % 2 == 0:
            even += 1
        else:
            odd += 1

    print("The number of odds are", odd)
    print("The number of evens are", even)


def main():
    i = 0
    while i == 0:
        n = 1

        count = int(input("Hello! How many inputs are you adding?: "))
        numbers = []

        while n <= count:
            adding_num = int(input("Add input " + str(n) + ":"))
            numbers.append(adding_num)
            n += 1

        summ(numbers)
        avg(numbers)
        maximum_minimum(numbers)
        count_even_odd(numbers)
        
        answer = input("Would you like to close it?(Y,N): ")
        if answer == "Y":
            print("Bye!")
            i += 1
        elif answer == "N":
            print("Ok then")

            
main()
