#Write a program that reads a text file, counts word frequency, and writes results to a new file

import string
from collections import Counter
def word_frequency_count(input_file, output_file):
  try:  
    with open(input_file, 'r') as file:
        text = file.read().lower()
        text = text.translate(str.maketrans('','', string.punctuation))
        words = text.split()
        word_count = Counter(words)
    with open(output_file, 'w') as file:
        for word,count in word_count.items():
            file.write(f"{word} : {count}\n")    
    print(f"Word frequency count written to {output_file}")
  except FileNotFoundError:
    print(f"Error: The file {input_file} was not found.")          
#Build a JSON-based to-do list app that saves and loads tasks from a file
import json
import os
class todolist():
    def __init__(self,filename):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)
    def add_task(self,task):
        self.tasks.append(task)
        self.save_tasks()
    def remove_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.save_tasks()
    def display_tasks(self):
        print("To-Do List:")
        for index,task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")            
        
#Create a custom exception class InvalidAgeError and raise it when age is negative
class InvalidAgeError(Exception):
    def __init__(self, message="Age cannot be negative"):
        self.message = message
        super().__init__(self.message)

def validate_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise InvalidAgeError("Age cannot be negative")
        print(f"Your age is {age}")
        return age
    except InvalidAgeError as e:
        print(e)
        return None
    except ValueError:
        print("Please enter a valid integer for your age.")
        return None

validate_age()

#Write a log writer that appends timestamped entries to a log file using context managers
from datetime import datetime
class Logger():
    def __init__(self,log_file):
        self.log_file = log_file
    def log(self,message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, 'a') as file:
            file.write(f"{timestamp} - {message}\n")
logger = Logger("app.log")
logger.log("Application started")
#Build a student record system that reads from a JSON file, allows updates, and saves changes back to the file
import json
import os
class StudentRecordSystem():
    def __init__(self,filename):
        self.filename = filename
        self.records = []
        self.load_records()
    def load_records(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.records = json.load(file)
    def save_records(self):
        with open(self.filename, 'w') as file:
            json.dump(self.records, file)
    def add_record(self,record):
        self.records.append(record)
        self.save_records()
    def update_record(self,index,new_record):
        if 0 <= index < len(self.records):
            self.records[index] = new_record
            self.save_records()
    def display_records(self):
        print("Student Records:")
        for index,record in enumerate(self.records, start=1):
            print(f"{index}. {record}")
    def update_student_record(self):
        self.display_records()
        try:
            index = int(input("Enter the record number to update: ")) - 1
            if 0 <= index < len(self.records):
                new_record = input("Enter the new record details: ")
                self.update_record(index, new_record)
                print("Record updated successfully.")
            else:
                print("Invalid record number.")
        except ValueError:
            print("Please enter a valid integer for the record number.")                        
system = StudentRecordSystem("student_records.json")
print("1. Add Record")
print("2. Update Record")
user_input = input("Enter your choice: ")
if user_input == "1":
    record = input("Enter the student record details: ")
    system.add_record(record)
elif user_input == "2":
    system.update_student_record()
                