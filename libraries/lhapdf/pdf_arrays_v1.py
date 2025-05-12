# (): Import LHDAPDF:
import lhapdf
print(lhapdf.version())
print(lhapdf.__version__)

# (): Import NumPy
import numpy as np


pdfset = 'NNPDF40_nlo_as_01180'
PDF_DATA = lhapdf.mkPDF(pdfset)

x_values = np.linspace(0.01, 0.3, 30)
print(x_values)
q_squared_values = np.array([2.4])
results = PDF_DATA.xfxQ2(2, x_values, q_squared_values)

print(results)

# Notice that `results` is actually an array with a SINGLE value despite us passing in
# an entire ARRAY into the damn function. That is so jank. Let's figure out what value
# it is returning. I am guessing it is the first or the last one. Probably the first.

print(PDF_DATA.xfxQ2(2, np.array([0.01]), q_squared_values))
print(PDF_DATA.xfxQ2(2, np.array([0.3]), q_squared_values))

# Yes. It returns only the FIRST EVALUATION if it sees and array in this case. That
# is BROKEN beyond belief. So, you have to do some sort of list comprehension and return
# a NumPy array if you want to continue to work with vectors and etc.