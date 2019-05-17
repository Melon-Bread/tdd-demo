#!/usr/bin/env python3
import argparse
import os
import platform
import shutil
import subprocess
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
        if not shutil.which('apt-get'):
            print("'apt-get' not found you may need to install the following packages manually:\n{}\n".format(packages))

        else:
            subprocess.call(['sudo', 'apt-get', 'update'])
            for package in packages:
                print('\nInstalling {}'.format(package))
                subprocess.call(['sudo', 'apt-get', 'install', '-y', package])

    elif OPERATING_SYSTEM == 'Windows':
        if not shutil.which('git'):
            print('Git not found in $PATH.\nPlease make sure you have Git installed\nhttps://gitforwindows.org/')
            sys.exit()

    elif OPERATING_SYSTEM == 'Darwin':
        if shutil.which('brew'):
            subprocess.call(['brew', 'update'])
            subprocess.call(['brew', 'install', 'git'])
        else:
            print('brew not found in $PATH.\nPlease make sure you have Homebrew installed\nhttps://brew.sh/')
            sys.exit()

    else:
        print("Operating system not supported")
        sys.exit()


def setup_venv():
    if not os.path.exists('env/'):
        print("Creating virtual environment")
        if OPERATING_SYSTEM is not "Windows":
            subprocess.call(['python3', '-m', 'venv', 'env'])
            print("Installing requirements")
            os.system('. env/bin/activate && pip install -r requirements.txt')
        else:
            # 'python' is the default Python 3 command on Windows
            subprocess.call(['python', '-m', 'venv', 'env'])
            print("Installing requirements")
            os.system('env\\Scripts\\activate.bat && pip install -r requirements.txt')


def launch_terminals():
    # TODO: Find out how to name terminal windows on Windows & macOS
    terminal_names = ['testing', 'git status', 'explore']
    # TODO: Convert the rcfiles into Python methods so they are more universal
    python_scripts = ['pytest.py',
                      'git-status.py',
                      'misc.py']

    for i in range(3):
        if OPERATING_SYSTEM == 'Linux':
            subprocess.Popen(['xterm', '-T', terminal_names[i],
                             '-e', 'python3', python_scripts[i]], stdout=subprocess.PIPE)


        elif OPERATING_SYSTEM == 'Windows':
            # TODO: Setup the command for opening a new terminal in windows
            subprocess.call(['start', '/wait', 'python', python_scripts[i]],
                            shell=True)

        elif OPERATING_SYSTEM == 'Darwin':
            # TODO: Add the commands to tell the terminals what to do
            subprocess.call(['open', '-W', '-a', 'Terminal.app', 'python3', '--args', python_scripts[i]])
            pass


if __name__ == "__main__":
    main()
