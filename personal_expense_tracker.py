import matplotlib.pyplot as plt
import csv as csv
import uuid as uuid
import pandas as pd


def remove_data_by_date(date):
    str_date = str(date)
    df = pd.read_csv("expense.csv")
    df = df[~df.apply(lambda row: row.astype(str).str.contains(str_date, case=False)).any(axis=1)]
    df.to_csv("expense.csv", index=False)
    print("Sucessfully deleted.")

def date_conversion_to_days(date):
    separate_date = date.split("/")
    year, month, day = separate_date
    converted_date = int(year) * 365 + int(month) * 30 + int(day)
    return converted_date


def uuid_generator():
   id = str(uuid.uuid4())
   return id


def csv_value_writer(a):
    with open('expense.csv', "a", newline="") as csvfile:
        value_writer = csv.writer(csvfile, delimiter=",")
        value_writer.writerow(a)


def check_input():
    i = input("Add expense? or Show report? or Delete expense or Exit?: ")
    try:
        if i == "Add expense":
            return 1
        elif i == "Show report":
            return 2
        elif i == "Exit":
            return 0
        elif i == "Delete expense":
            return 3
        else:
            print("Type correctly!")

    except ValueError:
        print("Invalid input")


def check_input_delete():
    i = input('Do you want to delete data by "Date" or "ID" or do you want to "Return"?: ')
    try:
        if i == "Date":
            return 1
        elif i == "ID":
            return 2
        elif i == "Return":
            return 0
        else:
            print("Type correctly!")
    except ValueError:
        print("Invalid input")


def main():
    print("Basic Expense Tracker")
    while True:
        i = check_input()

        if i == 1:

            print("Add the information")

            expense_catagory = input("What catagory does it follow?(Food, Transport, Shopping, Housing, Other): ")
            expense_amount = input("How much was the expense?(in euros): ")
            expense_date = input("When was it done?(year/month/day): ")

            converted_date = date_conversion_to_days(expense_date)
            expense_id = uuid_generator()

            combined_expense_data = (expense_catagory, expense_amount, converted_date, expense_id)
            csv_value_writer(combined_expense_data)

        elif i == 2:
            return
        
        elif i == 3:
            j = check_input_delete()

            if j == 1:
                get_input_date = input("What date?(Year/Month/Day):")
                conv_delete_day = date_conversion_to_days(get_input_date)
                remove_data_by_date(conv_delete_day)


        elif i == 0:
            print("Exiting program......")
            break


main()
