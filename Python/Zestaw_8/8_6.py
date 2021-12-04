import time

def P_dynamicznie(i, j):
	vals = [[]]
	vals[0].append(0.5)
	for x in range(1, i+1):
		vals[0].append(0)
	for row_i in range(1, j+1):
		vals.append([])
		vals[row_i].append(1.0)
		for col in range(1, i+1):
			vals[row_i].append(0.5 * (vals[row_i-1][col] + vals[row_i][col-1]))
	return vals[j][i]

def P_rekurencyjnie(i, j):
	if i == 0 and j == 0:
		return 0.5
	if j == 0:
		return 0
	if i == 0:
		return 1
	return 0.5 * (P_rekurencyjnie(i-1, j) + P_rekurencyjnie(i, j-1))

if __name__ == "__main__":
	print("Uzywajac metody rekurencyjnej:")
	print("P(3, 2) = ", P_rekurencyjnie(3, 2))
	print("P(9, 4) = ", P_rekurencyjnie(9, 4))
	print("P(12, 5) = ", P_rekurencyjnie(12, 5))

	print("Uzywajac metody dynamicznej:")
	print("P(3, 2) = ", P_dynamicznie(3, 2))
	print("P(9, 4) = ", P_dynamicznie(9, 4))
	print("P(12, 5) = ", P_dynamicznie(12, 5))

	print("Porownanie czasu dla 14 wywolan funkcji z takimi samymi argumentami:")
	rekurencyjnie_start = time.time()
	for i in range(14):
		P_rekurencyjnie(i, i)
	print("Czas dla metody rekurencyjnej: ", f"{time.time() - rekurencyjnie_start}s")
	
	dynamicznie_start = time.time()
	for i in range(13):
		P_dynamicznie(i, i)
	print("Czas dla metody dynamicznej: ", f"{time.time() - dynamicznie_start}s")
