import unittest 
from numseq.fib import fibonacci
from numseq.geo import sqr, triforce, cube
from numseq.prime import is_prime, primes

__author__="Swaav"

class TestFib (unittest.TestCase):
    def test_fib(self):
        fib_sequence = [0,1,1,2,3,5,8,13,21,34]
        for i, n in enumerate(fib_sequence):
            self.assertEqual(fibonacci(i), n)
  
print("Geometric numbers (square, triangle, cube)")
for i in range(10):
    print ("{}: {} {} {}".format(i, sqr(i), triforce(i), cube(i)))

print ("Primes")
prime_list = primes(1000)
for p in prime_list[-10:]:
    print (p)
print ("Is 999981 prime? {}".format(is_prime(999981)))
print ("Is 999983 prime? {}".format(is_prime(999983)))

if __name__ == "__main__":
    unittest.main()