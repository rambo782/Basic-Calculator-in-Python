def askForNumber() -> int:
	while True:
		number = input("Enter Number: ")
		if not number.isnumeric():
			print("Please enter a valid number!")
			continue
		else:
			break
	return int(number)

# This function just adds, so it's pretty much useless.
# def showResult(*nums) -> str:
	# return f"Result: {sum(nums)}"

def operationShowResults(operation,n1,n2) -> float:
	match operation:
		case "+":
			return n1+n2
		case "-":
			return n1-n2
		case "/":
			return n1/n2
		case "*":
			return n1*n2
		case _:
			return n1+n2


def main() -> None:
	num1 = askForNumber()
	op = str(input('Enter operation: '))
	num2 = askForNumber()
	print("Result: "+str(operationShowResults(op, num1, num2)))
	return None

if __name__ == '__main__':
	main()

