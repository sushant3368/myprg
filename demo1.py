a = list(map(int,input().rstrip().split()))
b = list(map(int,input().rstrip().split()))

def compareTriplets(a,b):
	
	if __name__ == '__main__':

		a_point = 0
		b_point = 0

		for k in range(len(a)):
			if a[k] > b[k]:
				a_point += 1
			elif a[k] < b[k]:
				b_point += 1
		print([a_point,b_point])

compareTriplets(a,b)