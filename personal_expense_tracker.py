import matplotlib.pyplot as plt
import csv as csv



def csv_value_writer(a):
    with open('expense.csv', "a", newline="") as csvfile:
        value_writer = csv.writer(csvfile, delimiter=",")
        value_writer.writerow(a)


def check_input():
    i = input("Add expense? or Show report? or Exit?: ")
    try:
        if i == "Add expense":
            return 1
        elif i == "Show report":
            return 2
        elif i == "Exit":
            return 0
        else:
            print("Add correctly")

    except ValueError:
        print("Invalid input")


def main():
    print("Basic Expense Tracker")
    while True:
        i = check_input()
        if i == 1:

            print("Add the information")

            expense_catagory = input("What catagory does it follow?(Food, Transport, Shopping, Housing, Other):")
            expense_amount = input("How much was the expense?(in euros):")
            expense_date = input("When was it done?(year/month/day):")

            separate_date = expense_date.split("/")
            year, month, day = separate_date
            converted_date = int(year) * 365 + int(month) * 30 + int(day)

            combined_expense_data = (expense_catagory, expense_amount, converted_date)
            csv_value_writer(combined_expense_data)
        elif i == 2:
            return


main()