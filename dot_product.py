import numpy as np



# # Example 1
# a = np.array([1, 2])
# b = np.array([3, 4])
# dot_product = np.dot(a, b)
# print("'a . b'=", dot_product)

a = np.array([2, 5, 7])
b = np.array([5, 9, 3])

scalar = 2
addition = a + b
subtraction = a - b
scalar_multiplication_a = a*scalar
scalar_multiplication_b = b*scalar

Dot_product = np.dot(a,b)

print(f"a + b = {addition.tolist()}")

print(f"a - b = {subtraction.tolist()}")

print(f"2a =  {scalar_multiplication_a.tolist()}")


print(f"2b =  {scalar_multiplication_b.tolist()}")

print(f"a . b = {Dot_product.tolist()}")
