import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x_range = np.linspace(-1.0, 1.0, 51)
y_range = np.linspace(-1.0, 1.0, 51)

X, Y = np.meshgrid(x_range, y_range)

Z = 1.12 * X**2 + 0.78 * Y**2
U, V  = 0.671 * X + 0.123 * Y, -0.85 * X + 0.73 * Y

x_flat = X.ravel()
y_flat = Y.ravel()
u_flat = U.ravel()
v_flat = V.ravel()
z_flat = Z.ravel()

def ellipse_ansatz(packed_vars, *function_parameter):
    x, y = packed_vars
    if len(function_parameter) == 2:
        a, b = function_parameter
        return a * x**2 + b * y**2
    if len(function_parameter) == 3:
        a, b, c = function_parameter
        return a * x**2 + b * y**2 + c * x * y
    if len(function_parameter) == 4:
        a, b, c, d = function_parameter
        return a * x**2 + b * y**2 + c * x * y + d
    else:
        raise ValueError("Unsupported number of parameters")
    
def two_dimensional_vector_field(packed_variables, *function_parameters):
    x, y = packed_variables
    if (len(function_parameters)) == 4:
        a, b, c, d = function_parameters
        u = a * x + b * y
        v = c * x + d * y
        vector_field_tuples = (u, v)
        return np.hstack(vector_field_tuples)
    else:
        raise ValueError("Unsupported number of parameters")

popt_ellipse, pcov_ellipse = curve_fit(
    ellipse_ansatz,
    xdata = (x_flat, y_flat),
    ydata = z_flat,
    p0 = [-0.3, -0.2])

print("> Best-fit parameters:", popt_ellipse)
print("> Covariance:", pcov_ellipse)

a_fit, b_fit = popt_ellipse

z_fit = ellipse_ansatz((X, Y), a_fit, b_fit)


fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot raw data surface
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.2, label='Raw Data')

# Plot fit surface
ax.plot_surface(X, Y, z_fit, cmap='plasma', alpha=0.3)

# Optional: Add legend manually since plot_surface doesn't support labels directly
from matplotlib.lines import Line2D
custom_lines = [
    Line2D([0], [0], color='purple', lw=4, label='Fitted Surface'),
    Line2D([0], [0], color='green', lw=4, label='Raw Data')
]
ax.legend(handles=custom_lines)

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Raw Data vs. Elliptic Fit")

plt.tight_layout()
plt.show()
plt.close()

xy = np.vstack((x_flat, y_flat))  # shape (2, N)
uv = np.hstack((u_flat, v_flat))  # shape (2N,)


fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

popt_vector_field, pcov_vector_field = curve_fit(
    two_dimensional_vector_field,
    xdata = xy,
    ydata = uv,
    p0 = [-0.3, -0.2, 4., 2.])

print("> Best-fit parameters:", popt_vector_field)
print("> Covariance:", pcov_vector_field)

xy_grid = np.vstack((X.ravel(), Y.ravel()))
uv_fit = two_dimensional_vector_field(xy_grid, *popt_vector_field)
u_fit = uv_fit[:X.size].reshape(X.shape)
v_fit = uv_fit[X.size:].reshape(X.shape)

plt.figure(figsize=(8, 6))
plt.quiver(X, Y, u_fit, v_fit, color='blue', alpha=0.6)
plt.title("Fitted Vector Field")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')
plt.grid(True)
plt.show()