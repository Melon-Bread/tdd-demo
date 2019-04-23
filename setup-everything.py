#!/usr/bin/env python3
import subprocess


def main():
    install_packages()


def install_packages():
    packages = ['python3-venv', 'meld', 'xterm']
    subprocess.call(['sudo', 'apt-get', 'update'])
    for package in packages:
        print('\nInstalling {}'.format(package))
        subprocess.call(['sudo', 'apt-get', 'install', '-y', package])


if __name__ == "__main__":
    main()
