from pathlib import Path
import pkgutil
import os

COMMANDS = []

for (_, name, _) in pkgutil.iter_modules([os.path.abspath(os.path.join(__file__, '../'))]):
    COMMANDS.append(name[4:len(name)])
