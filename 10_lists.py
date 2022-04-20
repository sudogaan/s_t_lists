>>> example=list()
>>> example2=[]
>>> primes=[2,3,5,7,11,13]
>>> primes.append(17)
>>> primes.append(19)
>>> primes
[2, 3, 5, 7, 11, 13, 17, 19]
>>> #in lists order is important
>>> primes[0] #view the first item
2
>>> # Slicing
>>> primes
[2, 3, 5, 7, 11, 13, 17, 19]
>>> primes[2:5]
[5, 7, 11]
>>> primes[0:6] #it will not include the final number
[2, 3, 5, 7, 11, 13]
>>> example=[128, True, "Alpha", 1.732, [64, False]]
>>> rolls=[4,7,2,7,12,4,7]
>>> rolls
[4, 7, 2, 7, 12, 4, 7]
>>> #even the repeated values are present in lists
>>> numbers=[1,2,3]
>>> letters=["a", "b", "c"]
>>> letters + numbers
['a', 'b', 'c', 1, 2, 3]
>>> # Concatenation
>>> numbers
[1, 2, 3]
>>> letters
['a', 'b', 'c']
>>> numbers + letters
[1, 2, 3, 'a', 'b', 'c']
