import math
import numpy as np

L = 39e-9  #  Murata LQW18AS39NG00D
C1 = 0.4e-12  # BF199 transistor internal capacitance
C2 =  4e-12  # variable capacitance


carrier_freq = 1 / (2 * math.pi * np.sqrt(L * ((C1*C2)/(C1 + C2))))

print(f"Frequency: {carrier_freq / 1e6} MHz")
