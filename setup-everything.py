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

        # Check to see if the Distro uses apt-get
        if subprocess.call(['which', 'apt-get']) == 0:
            print("'apt-get' not found you may need to install the following packages:\n{}\n".format(packages))

        else:
            subprocess.call(['sudo', 'apt-get', 'update'])
            for package in packages:
                print('\nInstalling {}'.format(package))
                subprocess.call(['sudo', 'apt-get', 'install', '-y', package])

    elif OPERATING_SYSTEM == 'Windows':
        # No extra packages are needed since venv is included with base windows install
        pass

    elif OPERATING_SYSTEM == 'Darwin':
        # TODO: Add macOS packages via homebrew
        pass

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

    for i in range(len(terminal_rcfiles)):
    while i < len(terminal_names):
        #subprocess.Popen(['xterm', '-T', terminal_names[i],
        #                  '-e', 'bash', '--rcfile', terminal_rcfiles[i]])
        subprocess.Popen(['bash', '--rcfile', terminal_rcfiles[i]],
                         creationflags=subprocess.CREATE_NEW_CONSOLE, shell=False)
            # Linux Kernel


if __name__ == "__main__":
    main()
