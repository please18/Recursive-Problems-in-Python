
def fibonacci(n):
  t = [0]*n
  t[0]  = 0
  t[1] = 1
  for i in range(2, n):
    fibonacci(i) = t[i-1] +t[i-2]
    
