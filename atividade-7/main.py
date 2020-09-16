import numpy as np
import sys
import os
from Operations import Operations

QC = np.pi/4
SIXTH = np.pi/3

print('P inicial = (2,0)')
print('Q inicial = (4,0)')
print('\n============== ex 1 ==============')
p = Operations(2, 0)
q = Operations(4, 0)
p.rotate(SIXTH)
q.rotate(SIXTH)
print("P final = %.2f %.2f" % (p.x, p.y))
print("Q final = %.2f %.2f\n" % (q.x, q.y))

print("============== ex 2 ==============")
p = Operations(2, 0)
q = Operations(4, 0)
p.reverse_translation(2, 0)
q.reverse_translation(2, 0)
p.rotate(SIXTH)
q.rotate(SIXTH)
p.translation(2, 0)
q.translation(2, 0)
print("P final = %.2f %.2f" % (p.x, p.y))
print("Q final = %.2f %.2f\n" % (q.x, q.y))

print("============== ex 3 ==============")
p = Operations(2, 0)
q = Operations(4, 0)
p.reverse_translation(3, 0)
q.reverse_translation(3, 0)
p.rotate(SIXTH)
q.rotate(SIXTH)
p.translation(3, 0)
q.translation(3, 0)
print("P final = %.2f %.2f" % (p.x, p.y))
print("Q final = %.2f %.2f\n" % (q.x, q.y))
