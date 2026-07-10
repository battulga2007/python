def insertion_sort_or_something_idk(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers

def main():
    numbers = [5, 2, 9, 1, 5, 6]
    sorted_numbers = insertion_sort_or_something_idk(numbers)
    print("Sorted numbers:", sorted_numbers)

main() 