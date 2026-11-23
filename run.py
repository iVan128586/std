
from os import system
import atexit

def on_exit():
    system("rm a.exe 2>nul")
atexit.register(on_exit)

def do(command: str):
    try:
        result = system(command)
    except KeyboardInterrupt:
        print("А всьо...")
        exit()
    if result != 0:
        print(f"Ошибка: {result} ({command})")
        exit()

def clear():
    do("cls")


clear()
do("clang test.c")
system("a.exe 123 -b dev")


# arr = []
# arr[0] = 1
