import fileinput
import re
import sys
from fractions import Fraction as frac

#Remove the string to integer conversion limit
sys.set_int_max_str_digits(0)

#Open a file and store it in a string
full = ""
for line in fileinput.input("E:\Portfolio\Programs\Extra - TE1/test.txt", encoding="utf-8"):
    full = full + line

#Remove all special characters and whitespace
full = re.sub('[^A-Za-z0-9]+', '', full)
full = full.lower()
numbers = []

#Convert all characters into a number and store it in a list
for letter in full:
    number = ord(letter) - 86
    numbers.append(number)

#Convert the list into a float
var = '0.'

for element in numbers:
    var += str(element)

print(frac(var))