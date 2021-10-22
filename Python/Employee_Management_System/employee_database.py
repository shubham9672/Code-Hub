import random
import csv
import os
import names
from tempfile import NamedTemporaryFile
import shutil


class employee:
    def __init__(self, first, last, salary):        # Constructor Definition
        # Class Instances
        self.fullname = first + " " + last
        self.first = first
        self.last = last
        self.salary = salary
        self.email = f"{first.lower()}" + f"{last.lower()}" + "@company.com"

    def input_data(self):
        # Class function to input data of a single employee
        self.first = input("Enter the first name of the employee: ")
        self.last = input("Enter the last name of the employee: ")
        self.fullname = self.first + " " + self.last
        self.salary = input("Enter the salary of the employee: ")
        self.email = f"{self.fullname}@company.com".lower().replace(" ", "")

        file_not_exists = not os.path.exists("employee_file.csv")   # If file does not exist, it returns 1

        # If file does not exist, write fieldnames as header and write the employee data to file
        if file_not_exists:
            with open('employee_file.csv', mode='a+') as employee_file:
                fields = ['Fullname', 'Email', 'Salary']
                employee_writer = csv.DictWriter(employee_file, fieldnames=fields)
                employee_writer.writeheader()
                employee_writer.writerow({'Fullname': self.fullname, 'Email': self.email, 'Salary': self.salary})

        # Otherwise, write employee data without writing header
        else:
            found = 0
            with open('employee_file.csv', 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:

                    # Checking if name already exists in the record
                    if row['Fullname'].upper().replace(" ", "") == self.fullname.upper().replace(" ", ""):
                        found = 1
                        print("Employee data exists.")
                        break
                    else:
                        continue

            # If name does not exist in the record, write employee data to file
            if found == 0:
                with open('employee_file.csv', mode='a') as employee_file:
                    fields = ['Fullname', 'Email', 'Salary']
                    employee_writer = csv.DictWriter(employee_file, fieldnames=fields)
                    if file_not_exists:
                        employee_writer.writeheader()
                    employee_writer.writerow({'Fullname': self.fullname, 'Email': self.email, 'Salary':self.salary})
            else:
                return

    # Function to write a given number of random records to file
    def random_data(self):

        file_not_exists = not os.path.exists("employee_file.csv")

        if file_not_exists:
            with open('employee_file.csv', mode='a+') as employee_file:
                fields = ['Fullname', 'Email', 'Salary']
                employee_writer = csv.DictWriter(employee_file, fieldnames=fields)
                employee_writer.writeheader()

        num = int(input("Enter number of random employees"))
        dict_emp = {}

        # Generating 'num' number of random employee records
        for val in range(num):
            name = f"emp_{val}"
            dict_emp[name] = employee(names.get_first_name(), names.get_last_name(), random.randint(10000, 20000))
            dict_emp[name].fullname = dict_emp[name].first + " " + dict_emp[name].last
            dict_emp[name].email = f"{dict_emp[name].fullname}@company.com".lower().replace(" ", "")

        # Checking if the names are already present in the record, before writing the generated records
        with open('employee_file.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                for val in dict_emp:
                    # If name is present pop that key from the dictionary
                    if row['Fullname'].upper().replace(" ", "") == dict_emp[val].fullname.upper().replace(" ", ""):
                        dict_emp.pop(val)

        # If file does not exist, write header has value 1
        with open('employee_file.csv', mode='a') as employee_file:
            fields = ['Fullname', 'Email', 'Salary']
            employee_writer = csv.DictWriter(employee_file, fieldnames=fields)

            # If file is empty, write fieldnames as header
            if file_not_exists:
                employee_writer.writeheader()

            # Writing all the records to file
            for val in dict_emp:
                employee_writer.writerow({'Fullname': dict_emp[val].fullname, 'Email':dict_emp[val].email, 'Salary':dict_emp[val].salary})


def menu():

    obj = employee('A', 'A', 1)

    print("\nEmployee Database Menu")
    print(
        """\n0.Enter Number of Random Employee Details
1.Enter Employee Details
2.Display Employee Details
3.Search Details of a Employee
4.Delete Details of Employee
5.Update Employee Details
6.Exit""")

    ch = int(input("Enter choice:"))

    if ch == 1:
        obj.input_data()
        print('Want to perform some other operation??? Y or N: ')
        inp = input()
        if inp == 'Y' or inp == 'y':
            menu()

    elif ch == 2:

        try:
            f = open('employee_file.csv', mode='r')

        except FileNotFoundError:
            print("File does not exist")
            menu()

        read_record()
        print('Want to perform some other operation??? Y or N: ')
        inp = input()
        if inp == 'Y' or inp == 'y':
            menu()
        else:
            exit()

    elif ch == 0:
        obj.random_data()
        menu()

    elif ch == 3:
        search_record()
        print('Want to perform some other operation??? Y or N: ')
        inp = input()
        if inp == 'Y' or inp == 'y':
            menu()
        else:
            exit()



    elif ch == 4:
        delete_record()
        print('Record Deleted ')
        print('Want to perform some other operation??? Y or N: ')
        inp = input()
        if inp == 'Y' or inp == 'y':
            menu()
        else:
            exit()

    elif ch == 5:
        update_record()

        print('Want to perform some other operation??? Y or N: ')
        inp = input()
        if inp == 'Y' or inp == 'y':
            menu()
        else:
            exit()


    elif ch == 6:
        print("Thank You !")
        exit()


# Function to print all records
def read_record():

    # Print records only when file exists
    file_exists = not os.path.exists("employee_file.csv")

    if file_exists != 1:

        print("\n")
        print("\nList of Employees\n")

        with open('employee_file.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f"Fullname".rjust(10) + "\t\t\t\t\t\t\t" f"Email".rjust(10) + "\t\t\t\t\t\t\t" + f"Salary".rjust(
                        10))

                line_count += 1
                print(
                    f"{row['Fullname'].upper().rjust(10)}\t\t\t\t{row['Email'].rjust(10)}\t\t\t\t{row['Salary'].rjust(10)}")
                line_count += 1

            print(f'Processed {line_count} lines.')

    else:
        print("\nFile does not exist")
        menu()


# Function to search a particular record from file
def search_record():

    search_fullname = input("Enter the full name of the employee... ").upper().replace(" ","")
    found = 0

    with open('employee_file.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:

            # Find record in file and print all records
            if search_fullname == row['Fullname'].upper().replace(" ",""):

                print("\n")
                print("\nList of Employees\n")

                # If it is the first row, print this row as header
                if line_count == 0:
                    print(
                f"Fullname".rjust(10) + "\t\t\t\t\t\t\t" f"Email".rjust(10) + "\t\t\t\t\t\t\t" + f"Salary".rjust(10))
                line_count += 1
                print(
                f"{row['Fullname'].upper().rjust(10)}\t\t\t\t{row['Email'].rjust(10)}\t\t\t\t{row['Salary'].rjust(10)}")
                found = 1
                line_count += 1
            else:
                continue
        if found == 0:
            print("Employee record does not exit")
            menu()

        # Display number of lines processed
        print(f'Processed {line_count} lines.')


# Function to update a particular record from file
def update_record():

    file_not_exists = not os.path.exists("employee_file.csv")
    if file_not_exists:
        print("File does not exist")
        return

    search_fullname = input("Enter the full name of the employee... ").upper()
    # Calling function to check whether the name exists in the record or not
    rec_exists = check_name(search_fullname)
    fields = ['Fullname', 'Email', 'Salary']

    # If record exists then proceed to update the employee data. We are using two files for updating the record
    if rec_exists == 1:
        filename = 'employee_file.csv'
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)

            for row in reader:

                # If name matches the record in file, display update menu
                if row['Fullname'].upper().replace(" ", "") == search_fullname.replace(" ", ""):
                    print('Updating data of employee', row['Fullname'].upper())

                    print("\nSelect the information you want to update:\n1.Fullname\n2.Email\n3.Salary\n")
                    choice = int(input("Your Choice: "))
                    if choice == 1:
                        new_fullname = input("\nEnter the new fullname: ")
                        name_exists = check_name(new_fullname)
                        if name_exists == 0:
                            row['Fullname'], row['Email'], row['Salary'] =  new_fullname,  row['Email'],  row['Salary']

                        else:
                            print("Employee name already exists in record.")
                            break
                    elif choice == 2:
                        new_email = input("\nEnter the new email: ")
                        row['Email'] = new_email
                        row['Fullname'], row['Email'], row['Salary'] =  row['Fullname'],  new_email,  row['Salary']

                    elif choice == 3:
                        new_salary = int(input("\nEnter the new salary: "))
                        row['Fullname'], row['Email'], row['Salary'] =  row['Fullname'],  row['Email'],  new_salary

                    else:
                        print("Invalid Choice..Returning to Menu")

                # Writing row to file
                row = {'Fullname': row['Fullname'], 'Email': row['Email'], 'Salary': row['Salary']}
                writer.writerow(row)

        # Making the temporary file as our original file
        shutil.move(tempfile.name, filename)
        return

    else:
        print("Employee does not exist")
        menu()


# Function to delete a particular record from file
def delete_record():

    file_not_exists = not os.path.exists("employee_file.csv")
    if file_not_exists:
        print("File does not exist")
        return

    search_fullname = input("Enter the full name of the employee... ").upper()
    rec_exists = check_name(search_fullname)
    fields = ['Fullname', 'Email', 'Salary']
    if rec_exists == 1:
        filename = 'employee_file.csv'
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                # Writing every record except the record we want to delete to our temporary file
                if row['Fullname'].upper().replace(" ", "") != search_fullname.replace(" ", ""):

                    row['Fullname'], row['Email'], row['Salary'] = row['Fullname'], row['Email'], row['Salary']
                    row = {'Fullname': row['Fullname'], 'Email': row['Email'], 'Salary': row['Salary']}
                    writer.writerow(row)

        shutil.move(tempfile.name, filename)
        return

    else:
        print("Employee does not exist")
        return


# Function to check whether a name exists in file or not
def check_name(new_fullname):
    found = 0
    with open('employee_file.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Fullname'].upper().replace(" ", "") == new_fullname.upper().replace(" ", ""):
                found = 1
                return 1
            else:
                continue
    if found == 0:
        return 0


menu()
