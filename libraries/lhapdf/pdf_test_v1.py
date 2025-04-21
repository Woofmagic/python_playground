# (): Import LHDAPDF:
import lhapdf
print(lhapdf.version())
print(lhapdf.__version__)

# (): Import NumPy
import numpy as np

# (): Import matplotlib:
import matplotlib.pyplot as plt

# (): This will not work unless you have locally installed NNPDF40_nlo_as_01180:
pdf_function = lhapdf.mkPDF("NNPDF40_nlo_as_01180")

# (): What will this return? array, int, float, ...?
print(pdf_function.xfxQ2(21, 1e-3, 1e4)) # returns a float

# (): Here is some hidden data:
print(pdf_function.flavors()) # list of ints (labels for something)

# (): And this will evaluate xf(x, Q^{2}) for each "flavor type" at a given x and Q^{2}:
for pid in pdf_function.flavors():
    print(pdf_function.xfxQ(pid, 0.01, 91.2))

# (): Set up a meshgrid for evaluating the function:
x_values = np.linspace(0.01, 0.3, 300)
q_squared_values = np.linspace(0.1, 3.0, 300)
x_grid_values, q_squared_grid_values = np.meshgrid(x_values, q_squared_values)

# (): Notice that it DOES NOT LIKE how things are coded below: IT will throw an error:
# print(pdf_function.xfxQ(21, x_values, q_squared_values[0]))
# print(pdf_function.xfxQ(21, x_values, np.array([0.4])))

# (): What *IS* liked (which is jank) is the following approach:

# Here is what PyLint has to say about the line below:
# > Unnecessary use of a comprehension, use list(np.logspace(-7, 0, 5)) instead.
xs = [x for x in np.logspace(-7, 0, 5)]

# > Unnecessary use of a comprehension, use list(np.logspace(1, 4, 4)) instead.
qs = [q for q in np.logspace(1, 4, 4)]

gluon_xfs = np.empty([len(xs), len(qs)])

for ix, x in enumerate(xs):
    for iq, q in enumerate(qs):
        gluon_xfs[ix,iq] = pdf_function.xfxQ(21, x, q)

print(gluon_xfs)

# (): Since that works above, then it seems to me like it just can't handle NumPy arrays... Let's find out:
# print(pdf_function.xfxQ(21, [2, 3, 4, 5], [6, 7, 8, 9]))

# print(pdf_function.xfxQ(21, x_grid_values, q_squared_grid_values))

figure, axis = plt.subplots(1, 1, figsize = (10, 5))
axis.plot(gluon_xfs[0, :], qs)

# for flavor_key in pdf_function.flavors():
#     axis.plot(pdf_function.xfxQ(flavor_key, x_values, q_squared_values[0]))

plt.show()