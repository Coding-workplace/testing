def func1(k):
	count = 0
	def func2():
		nonlocal count
		if count<k:
			count+=1
			print(f"Count: {count} and K: {k}")
			func2()
	func2()

func1(10)
