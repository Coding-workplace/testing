def func1(k):
	count = 0
	def func2():
		print(f"Count: {count} and K: {k}")
		
	func2()

func1(10)
