# Discrete Mathematics Lab 2: DNF Generator

This project is a Discrete Mathematics assignment focused on generating the Disjunctive Normal Form (DNF) from a given boolean statement. It utilizes the Python programming language and libraries such as `ttg` and `pandas` to achieve this functionality.

## Requirements

- Python 3.x
- ttg library
- pandas library

## Installation

1. Clone the repository:


2. Navigate to the project directory

3. Install the required dependencies:

    pip install -r requirements.txt


## Usage

1. Run the program:

2. Enter the test case number when prompted.

3. Enter the boolean statement when prompted. Make sure to include spaces around literals.

4. The program will generate the DNF of the given boolean statement and save the output to a file named `OUTPUT_TC{test_case_number}.txt`.

## Example

Enter the test case number: 1
Enter the boolean statement: p ^ q

DNF of the given boolean statement is ( ~p ^ q ) v ( p ^ ~q )
