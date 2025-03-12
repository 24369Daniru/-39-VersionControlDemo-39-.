#Version 1
print("Hello World !")
# Version 2
name = input("Enter your name: ")
print("Hello, {name}!")
# Version 3
while True:
name = input("Enter your name (or 'exit' to quit): ")
if name.lower() == 'exit':
break
print("Hello, {name}!")
