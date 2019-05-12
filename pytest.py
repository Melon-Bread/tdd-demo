#!/usr/bin/env python3

import platform
import os

if platform.system == 'Windows':
    os.system('env\\Scripts\\activate.bat && py.test -f .')
else:
    os.system('. env/bin/activate && py.test -f .')