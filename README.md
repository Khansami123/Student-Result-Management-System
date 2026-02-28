# Student-Result-Management-System

# 🎓 Student Result Management System (Python OOP)

## 📌 Project Description
The Student Result Management System is a Python-based application built using Object-Oriented Programming (OOP) concepts. It automates the process of storing student marks, calculating totals, percentages, and assigning grades.

## 🎯 Problem Statement
Manual result calculation is time-consuming and prone to errors. This system automates the process using structured OOP principles.

## 👥 Users
- Teachers (Admin)
- Students

## ⚙️ System Features
- Add students
- Add subject marks
- Calculate total marks
- Calculate percentage
- Automatically assign grades
- Display student result summary
- Count total students

## 🏗️ System Architecture

### Class Structure

Person (Parent Class)
│
├── Student (Child Class)
│
Result (Handles calculations)
│
StudentManagementSystem (Controller)

## 🔗 Relationships

- Inheritance → Student inherits from Person
- Composition → Student contains a Result object
- Association → StudentManagementSystem manages multiple students

## 🧠 OOP Concepts Used

### ✅ Encapsulation
Marks stored as private attribute `_marks`

### ✅ Inheritance
Student class inherits from Person

### ✅ Polymorphism
`__str__()` method overridden

### ✅ Constructor
`__init__()` used in all classes

### ✅ Magic Methods
- `__str__()` → Display student result
- `__len__()` → Count total students

## ▶️ How to Run

1. Make sure Python is installed.
2. Download or clone this repository.
3. Run the file:

```bash
python student_result_system.py
```
## 🚀 Future Improvements

- Add database integration
- Add login authentication
- Build GUI using Tkinter
- Convert to web application (Flask/Django)
- Add AI-based performance prediction

## 👨‍💻 Author
Abdul Sami Khan
