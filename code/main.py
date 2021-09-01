import sys

sys.path.insert(1,'/home/robin/Internship_Toolchain/src')

from pomdp_solver import *

import stormpy.pars
from pycarl.cln.cln import Rational
import time

if __name__ == "__main__":
    path = "prism/reward_controlled_pomdp.prism"
    prop = open("prism/properties.pctl", "r").read()
    print(prop)
    policy = solve_pomdp(path, prop)
    for value in policy.parameter_values:
        print("{}: {}".format(value, policy.parameter_values[value]))