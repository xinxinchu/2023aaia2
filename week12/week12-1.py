n = int(input('�п�J1�Ӽ�:'))
def isPrime(n):
  for i in range(2,n):
    if n%i==0:
      return False
  return True

if isPrime(n): print('n�O���')
else: print('n���O���')
