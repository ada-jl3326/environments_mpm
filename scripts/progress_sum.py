from envtest import progress_sum, rand_array

a = rand_array((1000,))
result = progress_sum(a)
print("sum =", result)
