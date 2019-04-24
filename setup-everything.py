#!/usr/bin/env python3
import subprocess
import os


def main():
    install_packages()
    setup_venv()


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


if __name__ == "__main__":
    main()
