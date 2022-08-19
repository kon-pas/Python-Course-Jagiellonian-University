def odwracanie_rekurencyjnie(L, left, right):
	if left != right and left < right:
		(L[left], L[right]) = (L[right], L[left])
		odwracanie_rekurencyjnie(L, left+1, right-1)
	return L

def odwracanie_iteracyjnie(L, left, right):
	for offset in range(int((right-left)/2)):
		(L[left+offset], L[right-offset]) = (L[right-offset], L[left+offset])
	return L

if __name__ == '__main__':
	print(odwracanie_rekurencyjnie([1, 2, 3, 4, 5, 6, 7, 8], 2, 6))
	print(odwracanie_iteracyjnie([1, 2, 3, 4, 5, 6, 7, 8], 2, 6))
