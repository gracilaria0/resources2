# 6.a
print('6.a:')
X = 'Spam'
def func():
    print(X)
func()
print()

# 6.b
print('6.b:')
X = 'Spam'
def func():
    X = 'NI!'
func()
print(X)
print()

# 6.c
print('6.c:')
X = 'Spam'
def func():
    X = 'NI!'
    print(X)
func()
print(X)
print()

# 6.d
print('6.d:')
X = 'Spam'
def func():
    global X
    X = 'NI!'
func()
print(X)
print()

# 6.e
print('6.e:')
X = 'Spam'
def func():
    X = 'NI!'
    def nested():
        print(X)
    nested()
func()
print(X)
print()

# 6.f
print('6.f:')
del X
def func():
    X = 'NI!'
    def nested():
        nonlocal X
        X = 'Spam'
    nested()
    print(X)
func()