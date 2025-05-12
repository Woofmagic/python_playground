import numpy as np

fun_scalar = 0.039035096598833516
single_array = np.array([0.35443792, 0.35437575, 0.35418928, 0.35387873, 0.3534444, 0.35288677])
doubly_nested_array = np.array([[0.41246027]])

scalar_times_single_array = fun_scalar * single_array
scalar_times_doubly_nested_array = fun_scalar * doubly_nested_array
single_times_double_array = single_array * doubly_nested_array

print(f"> scalar * single array = {scalar_times_single_array}")
print(f"> scalar * double array = {scalar_times_doubly_nested_array}")
print(f"> single * double array = {single_times_double_array}")

print(f"> Should this be the same as above? {0.41246027 * single_array}")

# Seems like scalar multiplication in linear algebra: f * [A] = elementwise scalar multiplication.