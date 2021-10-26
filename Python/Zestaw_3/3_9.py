def get_list_sum_sequences(seq_arr):
	return [sum(element) for element in seq_arr]

if __name__ == "__main__":
	print(get_list_sum_sequences([[],[4],(1,2),[3,4],(5,6,7)]))
