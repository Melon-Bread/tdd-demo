#!/usr/bin/env python3
import subprocess
import os
import platform
import sys
import shutil

OPERATING_SYSTEM = platform.system()


def main():
    install_packages()
    setup_venv()
    launch_terminals()


def install_packages():
    if OPERATING_SYSTEM == 'Linux':
        packages = ['python3-venv', 'meld', 'xterm']

        # Check to see if the Distro uses apt-get
        if not shutil.which('apt-get'):
            print("'apt-get' not found you may need to install the following packages:\n{}\n".format(packages))

        else:
            subprocess.call(['sudo', 'apt-get', 'update'])
            for package in packages:
                print('\nInstalling {}'.format(package))
                subprocess.call(['sudo', 'apt-get', 'install', '-y', package])

    elif OPERATING_SYSTEM == 'Windows':
        if not shutil.which('git'):
            print('Git not found in $PATH.\nPlease make sure you have Git for Windows installed')
            sys.exit()

    elif OPERATING_SYSTEM == 'Darwin':
        # TODO: Add macOS packages via homebrew
        pass

    else:
        print("Operating system no supported")
        sys.exit()


def setup_venv():
    if not os.path.exists('env/'):
        print("Creating virtual enviorment")
        if OPERATING_SYSTEM is not "Windows":
            subprocess.call(['python3', '-m', 'venv', 'env'])
        else:
            # 'python' is the default Python 3 command on Windows
            subprocess.call(['python', '-m', 'venv', 'env'])

    print("Installing requirements")
    os.system('. env/bin/activate && pip install -r requirements.txt')


def launch_terminals():
    terminal_names = ['testing', 'git status', 'expore']
    terminal_rcfiles = ['pytest-window-bashrc',
                        'git-status-bashrc',
                        'misc-bashrc']

    for i in range(len(terminal_rcfiles)):
        if OPERATING_SYSTEM == 'Linux':
            # WSL Kernel
            if 'Microsoft' in platform.platform():
                subprocess.Popen(['cmd', '/c', 'start', 'bash'])

            # Linux Kernel
            else:
                subprocess.Popen(['xterm', '-T', terminal_names[i],
                                  '-e', 'bash', '--rcfile', terminal_rcfiles[i]])
        elif OPERATING_SYSTEM == 'Windows':
            # TODO: Setup the command for opening a new terminal
            subprocess.Popen([],
                             creationflags=subprocess.CREATE_NEW_CONSOLE,
                             shell=True)


if __name__ == "__main__":
    main()
