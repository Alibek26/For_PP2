#Exercise 1: Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

pattern = r'ab*'  # 'a' followed by 0 or more 'b's
test_strings = ["a", "ab", "abb", "b", "ba"]

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")
        
"""
Output:
Matched: a
Matched: ab
Matched: abb
"""

#Exercise 2: Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
pattern = r'ab{2,3}'
test_strings = ["a", "ab", "abb", "abbb", "abbbb"]

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")
        
"""
Output:
Matched: abb
Matched: abbb
"""

#Exercise 3: Write a Python program to find sequences of lowercase letters joined with a underscore.
pattern = r'[a-z]+_[a-z]+'
text = "hello_world python_code Test_123"

matches = re.findall(pattern, text)
print(matches)

"""
Output:
['hello_world', 'python_code']
"""

#Exercise 4: Write a Python program to find sequences of one upper case letter followed by lower case letters.
pattern = r'[A-Z][a-z]+'
text = "Hello World Python Code ABC D2E"
matches = re.findall(pattern, text)
print(matches)

"""
Output:
['Hello', 'World', 'Python', 'Code']
"""

#Exercise 5: Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
pattern = r'a.*b$'  # 'a' followed by anything, ending with 'b'
test_strings = ["ab", "acb", "axxxb", "b", "ba"]

for s in test_strings:
    if re.fullmatch(pattern, s):
        print(f"Matched: {s}")
        
"""
Output:
Matched: ab
Matched: acb
Matched: axxxb
"""

#Exercise 6: Write a Python program to replace all occurrences of space, comma, or dot with a colon.
text = "hello, world. this is python"
new_text = re.sub(r'[ ,.]', ':', text)
print(new_text)

"""
Output:
hello:world:this:is:python
"""

#Exercise 7: Write a python program to convert snake case string to camel case string.
def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

s = "this_is_snake_case"
print(snake_to_camel(s))

"""
Output:
thisIsSnakeCase
"""

#Exercise 8: Write a Python program to split a string at uppercase letters.
text = "HelloWorldPythonCode"
parts = re.findall(r'[A-Z][a-z]*', text)
print(parts)

"""
Output:
['Hello', 'World', 'Python', 'Code']
"""

#Exercise 9: Write a Python program to insert spaces between words starting with capital letters.
text = "HelloWorldPythonCode"
spaced_text = re.sub(r'([A-Z])', r' \1', text).strip()
print(spaced_text)

"""
Output:
Hello World Python Code
"""

#Exercise 10: Write a Python program to convert a given camel case string to snake case.
def camel_to_snake(s):
    # Insert underscore before uppercase letters, then lower all
    return re.sub(r'(?<!^)([A-Z])', r'_\1', s).lower()

camel = "thisIsCamelCase"
print(camel_to_snake(camel))

"""
Output:
this_is_camel_case
"""