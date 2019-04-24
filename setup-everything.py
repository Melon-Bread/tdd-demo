#!/usr/bin/env python3
import subprocess
import os
import platform
import sys

def main():
    install_packages()
    setup_venv()
    launch_terminals(platform.system())


def install_packages():
    packages = ['python3-venv', 'meld', 'xterm']

    subprocess.call(['sudo', 'apt-get', 'update'])
    for package in packages:
        print('\nInstalling {}'.format(package))
        subprocess.call(['sudo', 'apt-get', 'install', '-y', package])


def setup_venv():
    if not os.path.exists('env/'):
        print("Creating virtual enviorment")
        subprocess.call(['python3', '-m', 'venv', 'env'])

    print("Installing requrements")
    os.system('. env/bin/activate && pip install -r requirements.txt')


def launch_terminals(operating_system):
    terminal_names = ['testing', 'git status', 'expore']
    terminal_rcfiles = ['pytest-window-bashrc',
                        'git-status-bashrc',
                        'misc-bashrc']
   
    i = 0
    while i < len(terminal_names):
        if (operating_system == 'Linux'):
            subprocess.Popen(['xterm', '-T', terminal_names[i], 
                             '-e', 'bash', '--rcfile', terminal_rcfiles[i]])
            i += 1
        else:
            print("Operating system not supported")
            sys.exit()
            

if __name__ == "__main__":
    main()
