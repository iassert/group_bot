import os
import sys

dir_ = os.path.dirname(os.path.realpath(__file__))
dir_ = os.path.dirname(dir_)

sys.path.append(dir_)

from Handlers.main       import Main
from Registers.registers import *


if __name__ == "__main__":
    Main.main()
