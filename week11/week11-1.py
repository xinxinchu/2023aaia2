#week11-1.py
def func(n):
  if n ==1: return 1
  return n * func(n-1)
n = int(input('�п�J1�ӼƦr:'))
ans = func(n)
print('���׬O:', ans)
