import pandas as pd
import csv as csv
import hashlib as hl
import uuid as uuid


def deleteExaminfo(i):
    df = pd.read_csv("student_info.csv")

    x = df.loc[df['ID'] == str(i)]
    print(x)

    get_input = input("Would you like to continue?(y/n): ")

    while True:
        try:
            if get_input == "y":
                df = df.drop(df[x], inplace=True)
                df.to_csv('student_info.csv', index=False)
                return False

            elif get_input == "n":
                print("Exiting...")
                return False

        except ValueError:
            print("Invalid input")



def updateExaminfo(i):
    df = pd.read_csv("student_info.csv")

    x = df.loc[df['ID'] == str(i)]
    print(x)

    get_input = input("Would you like to continue?(y/n): ")

    try:
        if get_input == "y":
            grade_input = input("Input the grade you want change to: ")
            df.loc[df['ID'].str.contains(i), 'Grade'] = grade_input
            print(df)
            df.to_csv('student_info.csv', index=False).astype(str)

        elif get_input == "n":
            print("Exiting...")

    except ValueError:
        print("Invalid input")


def getLessonReport(i):
    df = pd.read_csv("student_info.csv")
    x = df.loc[df['Subject'] == str(i)]
    print(x)
    

def getStudentReport(i):
    x = pd.read_csv("student_info.csv")
    y = x.loc[x['Name'] == str(i)]
    print(y)


def addStudentinfo(j, k):
    while True:
        i = input("Do you want to continue or exit?: ")

        try:
            if i == "continue":
                subject = input("Can you add the subject?: ")
                grade = input("Can you add the grade?: ")
                exam_date = input("Can you add the exam date?: ")
                student_id = str(uuid.uuid4())
                combinedData = (j, k, subject, grade, exam_date, student_id)
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
            print("")
            print("Welcome to probably the worst student info managing program ever made on this planet earth.")
            print("There are few commands you can give")
            print("1) Add : (You can add the record of the student) ")
            print("2) View : (You can view the record of a specified student with their ID) ")
            print("3) Show report : (You can view the lesson grade related reports) ")
            print("4) Update : (You can modify the info about already existing student data)")
            print("5) Delete : (You can delete the info about that specific student data")
            print("6) Exit : (To exit, duh, what did you even think what would this do?)")
            print("")
            
        elif i == "Add":
            print("Enter the following information")
            get_Student_ID = input("Add Student ID: ")
            get_Student_Name = input("Add Student Name: ")

            addStudentinfo(get_Student_ID, get_Student_Name)

        elif i == "View":
            get_student_ID_view = input("Enter the student ID: ")
            getStudentReport(get_student_ID_view)

        elif i == "Show report":
            get_Lesson = input("Enter the lesson that you want to the report of: ")
            getLessonReport(get_Lesson)

        elif i == "Update":
            get_student_update = input("Add ID to update: ")
            
            updateExaminfo(get_student_update)

        elif i == "Delete":
            get_student_delete = input("Add ID to delete: ")
            deleteExaminfo(get_student_delete)

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
