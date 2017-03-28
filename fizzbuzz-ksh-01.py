def fizzbuzz(n):

	if n % 3 == 0 and n % 5 == 0:
		return 'FizzBuzz'
	elif n % 3 == 0:
		return 'Buzz'
	elif n % 5 == 0:
		return 'Fizz'
	else:
		return str(n)

print "\n".join(fizzbuzz(n) for n in xrange(1, 100))
