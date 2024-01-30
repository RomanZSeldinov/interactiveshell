import ishtools
import os
import sys
import time

working_directory = os.getcwd()
def ls():
    global working_directory
    listdir = os.listdir(working_directory)
    for i in listdir:
        print(i)


def cd():
    global working_directory
    pathdir = input("Path: ")
    fullpath = working_directory + "/" + pathdir
    isdir = os.path.isdir(fullpath)
    if (isdir == True):
        working_directory = fullpath
    else:
        print("Directory not found.")

def cddotdot():
    global working_directory
    working_directory = os.path.abspath(os.path.join(working_directory, os.pardir))

def pwd():
    global working_directory
    print(working_directory)

commands = {
    "ls":ls,
    "cd":cd,
    "cd ..":cddotdot,
    "pwd":pwd,
    "mkdir":ishtools.mkdir,
    "m":ishtools.loadmod,
    "loadmod":ishtools.loadmod,
    "help":ishtools.help,
    "exit":ishtools.exit
}

def console():
    
    global working_directory
    print(r"""
                                                                                                                                                    
,--.,--.  ,--.,--------.,------.,------.   ,---.   ,-----.,--------.,--.,--.   ,--.,------.                 ,---.  ,--.  ,--.,------.,--.   ,--.    
|  ||  ,'.|  |'--.  .--'|  .---'|  .--. ' /  O  \ '  .--./'--.  .--'|  | \  `.'  / |  .---'                '   .-' |  '--'  ||  .---'|  |   |  |    
|  ||  |' '  |   |  |   |  `--, |  '--'.'|  .-.  ||  |       |  |   |  |  \     /  |  `--,                 `.  `-. |  .--.  ||  `--, |  |   |  |    
|  ||  | `   |   |  |   |  `---.|  |\  \ |  | |  |'  '--'\   |  |   |  |   \   /   |  `---.                .-'    ||  |  |  ||  `---.|  '--.|  '--. 
`--'`--'  `--'   `--'   `------'`--' '--'`--' `--' `-----'   `--'   `--'    `-'    `------'                `-----' `--'  `--'`------'`-----'`-----' 
                                                                                                                                                    
                                          
""")
    print("Welcome to Interactive Shell!")      
        
    while True:
        command = input("Interactive Shell: ")
        if command in commands:
            commands[command]()
        else:
            print("Command not found. Type 'help' for a list of commands.")
