# -*- coding: UTF-8 -*-
"""
Short script for rewriting a set of BayeSN model files into YAML format. Usage:
	python convert_to_yaml.py DIRECTORY
"""

import sys
import numpy as np
import ruamel.yaml as yaml

path = sys.argv[1]

data = {}

# Deals with scalar
param = np.genfromtxt(path + "/M0_sigma0_RV_tauA.txt")
data["M0"] = float(param[0])
data["SIGMA0"] = float(param[1])
data["RV"] = float(param[2])
data["TAUA"] = float(param[3])

# Deals with vectors
for name in ["tau_knots", "l_knots", "W0", "W1", "L_Sigma_epsilon"]:
	param = np.genfromtxt(path + "/" + name + ".txt")
	data[name.upper()] = param.tolist()

with open(path + "/BAYESN.YAML", "w") as file:
	yaml.dump(data, file)
