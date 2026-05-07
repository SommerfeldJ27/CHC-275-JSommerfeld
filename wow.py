import os
import glob

files = glob.glob("../")
programs = [compile(f) for f in files]


exec()
