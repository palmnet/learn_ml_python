
from sklearn.datasets import load_boston
import numpy as np
boston = load_boston()

x = boston.data[:,5]
x = np.array([[v] for v in x])
import pdb; pdb.set_trace() # BREAKPOINT


