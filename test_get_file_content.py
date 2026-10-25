from functions.get_file_content import get_file_content

a = get_file_content("calculator", "lorem.txt")
b = get_file_content("calculator", "main.py")
c = get_file_content("calculator", "pkg/calculator.py")
d = get_file_content("calculator", "/bin/cat")
e = get_file_content("calculator", "pkg/does_not_exist.py")

print(f"lorem.txt lenght: {len(a)}")
print(f"lorem.txt truncated: {'truncated' in a}")
print(b)
print(c)
print(d)
print(e)
