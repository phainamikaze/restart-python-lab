import os

print(os.getcwd())
os.mkdir("testdir")
print(os.listdir())
os.rmdir("testdir")
print(os.listdir())

print(os.getlogin())
print(os.system("whoami"))