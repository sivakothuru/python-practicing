# importing argv
from sys import argv

script, input_file = argv

# function for reading the file data
def print_all(f):
    print f.read()

# function where are again going to starting position of string
def rewind(f):
    f.seek(0)

# function to read a single line
def print_a_line(line_count, f):
    print line_count, f.readline()

# calling function
current_file = open(input_file)

print "First let's print the whole file:\n"

# print_all function call
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# rewind function call
rewind(current_file)

print "Let's print three lines:"

current_line = 1
# print_a_line function call
print_a_line(current_line, current_file)

current_line += 1
# print_a_line function call
print_a_line(current_line, current_file)

current_line += 1
# print_a_line function call
print_a_line(current_line, current_file)