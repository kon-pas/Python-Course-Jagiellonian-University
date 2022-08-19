def init_listening_print_cubed_number():
	while True:
		reply = input("Wprowadz liczbe rzeczywista: ")
		if reply == "stop":
			break
		try:
			number = float(reply)
		except ValueError:
			print("To nie jest liczba rzeczywista!")
		else:
			print(str(number) + '^3 = ' + str(number ** 3))
      
if __name__ == "__main__":
	init_listening_print_cubed_number()
