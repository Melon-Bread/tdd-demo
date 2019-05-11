#!/usr/bin/env python3

import platform
import subprocess


if platform.system == 'Windows':
    # TODO: Add 'watch' windows equivalent
    pass
else:
    subprocess.Popen(['watch', 'git', 'status'])