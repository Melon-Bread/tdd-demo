#!/usr/bin/env python3
import subprocess


def main():
    print("hello world")
    install_packages()


def install_packages():
    subprocess.call(['sudo', 'pacman', '-S', 'git'])
    subprocess.call(['sudo', 'apt-get', 'install', 'python3-venv'])


if __name__ == "__main__":
    main()
