# 5.a
def func(a, b=4, c=5):
    print(a, b, c)

func(1, 2)

# 5.b
def func(a, b, c=5):
    print(a, b, c)
func(1, c=3, b=2)

# 5.c
def func(a, *pargs):
    print(a, pargs)
func(1, 2, 3)

# 5.d
def func(a, b, c=3, d=4):
    print(a, b, c, d)
func(1, *(5, 6))