import sys
import string



def mapper():
  num_count=0
  prime_count=0
  num_sum=0
  for line in sys.stdin:
    num = line.strip()
    #for word in words:
    num_count+=1
    num_sum+=int(num)
    if(isprime(int(num))):
      prime_count+=1
      #print1 num
  print 'NumCount\t%s'%num_count
  print 'NumSum\t%s'%num_sum
  print 'PrimeCount\t%s'%prime_count

def isprime(num):
  known_primes=[2,3,5,7]
  if num in known_primes:
    return False
  if((num%2)==0 & (num%3)==0):
    return False
  for i in range(2,int(pow(int(num),0.5))+1):
    if((num%i)==0):		
      return False
  return True


mapper()
