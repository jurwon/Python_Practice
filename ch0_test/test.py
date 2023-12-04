a = 10
b = 3
print((int)(a/b))

#동적 할당
def f2(x):
  x = x+1
  return x

def f1(x):
  x = x*2
  y = f2(x)
  return y

y = 5
z = f1(y)