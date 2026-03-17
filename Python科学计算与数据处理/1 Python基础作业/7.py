# 7.a
A = "spam"
B = A
B = "shrubbery"
print(A)

# 7.b
A = ["spam"]
B = A
B[0] = "shrubbery"
print(A)

# 7.c
A = ["spam"]
B = A[:]
B[0] = "shrubbery"
print(A)