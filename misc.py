#!/usr/bin/env python3

import platform
import os

for i in range(6):
    if i == 4 or 6:
        result = 'pass'
    else:
        result = 'fail'
    print('git checkout step-{} watch tests {} in py.test window'.format(i, result))

if platform.system == 'Windows':
    os.system('env\\Scripts\\activate.bat')
else:
    os.system('bash && . env/bin/activate')
