# Track Student Grades
A Python-based student grades tracker built with Object-Oriented Programming (OOP), featuring statistical analysis and data visualization.

## Features
- Add Students: Add regular students or honor students.
- Add Grades: Assign grades to students across multiple subjects.
- View Student: Display a student's grades, average, and letter grade.
- Class Report: View all students sorted by their average (descending).
- Top Students: Display the top 3 students in the class.
- Class Statistics: Show class average, highest/lowest average, and pass/fail counts.
- Filter by Grade: List all students who achieved a letter grade of "A".
- Compare Students: Compare two students' scores in a specific subject.
- Visual Charts: Generate bar charts (subject averages) and pie charts (grade distribution) using Matplotlib.

## Technologies Used
- Language: Python
- Concepts: Object-Oriented Programming (Inheritance, Polymorphism, Encapsulation)
- Libraries: Matplotlib (for data visualization)
- Data Structures: Dictionaries, Lists, Sets

## Project Structure
- `main.py`: The main program with the user interface (CLI menu) and input handling.
- `models.py`: Contains the core classes:
  - `Student`: Represents a regular student with a name and grades.
  - `HonorStudent`: Inherits from `Student` and adds scholarship eligibility.
  - `GradeBook`: Manages a collection of students and provides reports and statistics.

## How to Run
1. Make sure Python 3 is installed on your machine .
2. Install the required library (Matplotlib)
3. Clone this repository or download the files.
4. Open main.py in the project folder.
5. Run the program by executing: python main.py
6. Follow the on-screen menu to interact with the system.

## Author
Farah Almomani
- GitHub: [@Farah-Almomani](https://github.com/Farah-Almomani)
