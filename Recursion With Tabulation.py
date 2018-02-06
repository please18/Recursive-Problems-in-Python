
def fibonacci(n):
  table = [0]*(n + 1)
  table[0]  = 0
  table[1] = 1
  for i in range(2, n+1):
    table[i] = t[i-1] +t[i-2]
  return table[n] 
    
