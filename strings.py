# int, float and string
name = "Emobilis"
# print(type(name))
print(name * 3)
#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
# You can use three double quotes:
a = """Lorem ipsum dolor sit amet."""
print(a)
b = '''Lorem ipsum dolor sit amet.'''
print(b)
f_name = "Tom"
l_name = "Ross"
full_name = f_name + " " + l_name + " " +"This are my names"
print(f_name.upper())
print(l_name.lower())

print("jack jill".title())

age = "20"
print(age.isnumeric()) #checks if age is numeric
# string slicing
b = "Hello, World!"#Gets characters from position 2 to position 5 (5 exclude):
print(b[2:5])
b = "Hello, World!" # gets characters from the start to position 5 (excluded)
print(b[:5])
