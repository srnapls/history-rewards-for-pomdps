import sys

sys.path.insert(1,'/home/robin/Internship_Toolchain/src')

from pomdp_solver import *
from induced_POMDP import *

import stormpy.pars
from pycarl.cln.cln import Rational
import time

def run_singular_pomdp(T, R):
    model = induced_POMDP("prism/obstacle.prism", R, True, T)
    print("reading prism file finished")
    model.create_prism_file()
    path = "prism/reward_controlled_pomdp.prism"
    prop = open("prism/properties.pctl", "r").read()
    policy = solve_pomdp(path, prop)
    #for value in policy.parameter_values:
    #    print("{}: {}".format(value, policy.parameter_values[value]))

if __name__ == "__main__":
    
    # N = 5
    R = {"20*3":100, "20*10*3":50, "20*10*10*3":25}
    print ("N = 5")
    # N = 10
    #R = {"31*0":100, "31*21*0":50, "31*21*21*0":25}
    T = [20,40,60,80,100,120,140,160,180,200]
    #print("N=10")
    for t in T:
        print("===============================")
        print("T =" + str(t))
        run_singular_pomdp(t, R)