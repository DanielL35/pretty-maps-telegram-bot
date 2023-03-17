import os

os.chdir("cache")
[os.remove(f) for f in os.listdir()]