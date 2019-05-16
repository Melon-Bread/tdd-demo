#!/usr/bin/env python3

import platform
import os

for i in range(6):
    print('git checkout step-{}'.format(i))

if platform.system == 'Windows':
    os.system('env\\Scripts\\activate.bat')
else:
    os.system('bash && . env/bin/activate')
