from functions.get_files_info import get_files_info

a = get_files_info("calculator", ".")
b = get_files_info("calculator", "pkg")
c = get_files_info("calculator", "/bin")
d = get_files_info("calculator", "../")

print(a)
print(b)
print(c)
print(d)
