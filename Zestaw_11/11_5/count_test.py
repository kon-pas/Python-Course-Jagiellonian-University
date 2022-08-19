import lists
import count

if __name__ == '__main__':
	print(count.counting_sort(lists.random_list(20)))
	print(count.counting_sort(lists.almost_sorted_list(20)))
	print(count.counting_sort(lists.reversed_almost_sorted_list(20)))
	print(count.counting_sort(lists.random_list_with_duplicates(20)))
