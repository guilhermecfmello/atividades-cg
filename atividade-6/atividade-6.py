import numpy as np
import sys
import os
from Point import *

TRINTA = np.pi/6
SESSENTA = np.pi/3
QC = np.pi/4

print("P = (1,1) inicial")
p = Point(1, 1)
p.translation(-1, 0)
p.scale(1, 2)
p.rotate(QC)
p.show()

print("Q = (3,7) inicial")
q = Point(3, 7)
q.translation(-1, 0)
q.scale(1, 2)
q.rotate(QC)
q.show()
