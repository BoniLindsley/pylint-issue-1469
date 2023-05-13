#!/usr/bin/env python3

from bsyncio.subprocess import PClose
okay: PClose

import bsyncio.subprocess
_not_okay:bsyncio.subprocess.PClose
# E1101: Module 'subprocess' has no 'PClose' member (no-member)
