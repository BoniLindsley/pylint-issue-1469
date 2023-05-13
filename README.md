Minimal working example of
[pylint/issue/1469 - False positive no-memberon asyncio.subprocess.create\_subprocess\_exec](https://github.com/pylint-dev/pylint/issues/1469).

Run `pylint issue.py`.

## Description

As of writing,
[typestub](https://github.com/python/typeshed/blob/9c212cdf5c1573f71d4fa55f02cfd058e2a4a6e3/stdlib/asyncio/__init__.pyi#L13)
for `asyncio` uses wildcard imports.

```py
from .subprocess import *
```

The module it imports from is then `asyncio/subprocess.pyi`.
Its [typestub](https://github.com/python/typeshed/blob/9c212cdf5c1573f71d4fa55f02cfd058e2a4a6e3/stdlib/asyncio/subprocess.pyi#L1)
contains

```py
import subprocess
```

Perhaps this confuses Pylint.
