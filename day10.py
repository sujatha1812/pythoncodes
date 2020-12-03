# string contains only a set of characters#
import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))


#certain string match ab

import re
def text_match(text):
        patterns = 'ab*?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('not found match!')

print(text_match("The abd quick brown fox jumps over the laby dog."))
print(text_match("Python Exercises."))

#number at the end of the sentence

import re
def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False

print(end_num('abcd45'))
print(end_num('sdjdkdlmdlm3.4'))

#find the length of number in a string

import re
results = re.finditer(r"([0-9]{1,3})", "Exercises number 11, 1, 123, 132, and 445 are important")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))

#string contain only upper case letter

import re
print(bool(re.match('^[A-Z]+$', '123aAbc')))
print(bool(re.match('^[A-Z]+$', 'ABC')))
