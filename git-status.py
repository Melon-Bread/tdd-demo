#!/usr/bin/env python3

import os
import platform


if platform.system == 'Windows':
    # TODO: Add 'watch' windows equivalent
    pass
else:
    os.system('watch git status')