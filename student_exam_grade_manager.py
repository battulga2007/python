import pandas as pd
import csv as csv
import hashlib as hl


def bare_bone_part_of_adding_info_to_the_csv_file_i_think_but_i_do_not_know_so_plz_help(j, k):
    while True:
        i = input("Do you want to continue or exit?: ")
        try:
            if i == "continue":
                subject = input("Can you add the subject?: ")
                grade = input("Can you add the grade?: ")
                exam_date = input("Can you add the exam date?: ")
                combinedData = (j, k, subject, grade, exam_date)
                add_Info(combinedData)
            elif i == "exit":
                print("Exiting....")
                return False
            else:
                print("Invalid Command")
        except ValueError:
            print("Invalid input")



def add_Info(i):
    with open('student_info.csv', "a", newline="") as csvfile:
        value_writer = csv.writer(csvfile, delimiter=",")
        value_writer.writerow(i)



def first_input_check(i):
    try:
        if i == "help":
            print("Welcome to probably the worst student info managing program ever made on this planet earth.")
            print("There are few commands you can give")
            print("1) Add : (You can add the record of the student) ")
            print("2) View (Student ID) : (You can view the record of a specified student with their ID) ")
            print("3) Show report (Lesson) : (You can view the lesson grade related reports) ")
            print("4) Update (Student ID) : (You can modify the info about already existing student data)")
            print("5) Delete (Student ID) : (You can delete the info about that specific student)")
            print("6) Exit : (To exit, duh, what did you even think what would this do?)")
            print("""
""")
            
        elif i == "Add":
            print("Enter the following information")
            get_Student_ID = input("Add Student ID: ")
            get_Student_Name = input("Add Student Name: ")
            bare_bone_part_of_adding_info_to_the_csv_file_i_think_but_i_do_not_know_so_plz_help(get_Student_ID, get_Student_Name)

        elif i == "View":
            get_student_ID_view = input("Enter the student ID: ")

        else:
            print("Invalid command")
    except ValueError:
        return NameError



def main():
    print("Student Info Manager")
    
    while True:
        get_first_input = input("What do you wish to do?(Type 'help' if you are confused): ")
        first_input_check(get_first_input)



main()
