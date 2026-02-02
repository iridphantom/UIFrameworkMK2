import pathlib

from datetime import datetime
from pathlib import Path


time = datetime.now().strftime('%Y%m%d_%H%M%S_%f')[:-3]
print(time)
print(type(time))

path1 = Path(__file__).parent
path2 = pathlib.Path(__file__).parents[0]

print(path1)
print(path2)