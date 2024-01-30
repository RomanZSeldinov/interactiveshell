import os
import sys
import time


def ls():
    listdir = os.listdir(input("Path: "))
    for i in listdir:
        print(i)

def loadmod():
    modpath = input("Path: ")
    try:
        with open(modpath) as f2:
            exec(f2.read())
    except IOError:
        print("Error while reading file.")

def mkdir():
    path = input("Path: ")
    if not os.path.exists(path):
        os.mkdir(path)
        
def help():
    print("ls - Show directory entries")
    print("cd - Open Directory")
    print("mkdir - Make Directory")
    print("hfmi - Humanity FileManager Improved")
    print("cf - Create file")
    print("vf - View file")
    print("wf - Write file")
    print("m - Load mod")
    print("help - Show this help message")
    print("exit - Exit PyOS")

def exit():
    sys.exit()
