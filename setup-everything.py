#!/usr/bin/env python3
import subprocess
import os
import platform
import sys

OPERATING_SYSTEM = platform.system()


def main():
    install_packages()
    setup_venv()
    launch_terminals()


def install_packages():
    if OPERATING_SYSTEM == 'Linux':
        packages = ['python3-venv', 'meld', 'xterm']

        subprocess.call(['sudo', 'apt-get', 'update'])
        for package in packages:
            print('\nInstalling {}'.format(package))
            subprocess.call(['sudo', 'apt-get', 'install', '-y', package])
    else:
        print("Operating system no supported")
        sys.exit()


def setup_venv():
    if not os.path.exists('env/'):
        print("Creating virtual enviorment")
        subprocess.call(['python3', '-m', 'venv', 'env'])

    print("Installing requrements")
    os.system('. env/bin/activate && pip install -r requirements.txt')


def launch_terminals():
    terminal_names = ['testing', 'git status', 'expore']
    terminal_rcfiles = ['pytest-window-bashrc',
                        'git-status-bashrc',
                        'misc-bashrc']

    i = 0
    while i < len(terminal_names):
        #subprocess.Popen(['xterm', '-T', terminal_names[i],
        #                  '-e', 'bash', '--rcfile', terminal_rcfiles[i]])
        subprocess.Popen(['bash', '--rcfile', terminal_rcfiles[i]],
                         creationflags=subprocess.CREATE_NEW_CONSOLE, shell=False)
        i += 1


if __name__ == "__main__":
    main()
