# Statistical Calculator
"""
Psedocode
--------------
This program will recieves 5 numbers from the user.\
Then it uses these numbers to to calculate the mean, median, maximum and minimum values.
It also calculates and displays the variance and standard deviation of the data.
It the allows you to replace the items in the data entered by you
Then saves the data in a text file called statistics
"""


def display_menu():# Displays the menu whenever called on the main function
    print("\nMenu:")
    print("1. Add items/elements.")
    print("2. Five number summary.")
    print("3. The mean.")
    print("4. Standard deviation and variance.")
    print("5. Replace items or elements.")
    print("6. Saving the items in a text file.")
    print("7. Display data.")
    print("8. Search for a number.")
    print("9. Delete number.")
    print("10. Range and IQR")
    print("11. Exit")


def add_elements():
    numbers = []
    # Asks the user the number of items they wanna check for.
    inputs = int(input("Enter the total number of items (n): "))

    # Loop to ask /prompt the user enter 5 numbers.
    for i in range(inputs):
        num = int(input(f"Enter a numeber {i + 1}: "))
        numbers.append(num)

    numbers.sort()# Sorts the numbers from smallest to biggest.
    print("The elements have been added successfully.")

    return numbers


def five_number_summary(numbers):

    maximum = max(numbers)# Finds the maximum value from the list of numbers
    minimum = min(numbers)# Finds the minimum value from the list of numbers


    # Determining the position of the median/middle term (q2)
    index = (len(numbers) + 1) // 2 # th position
    position = index - 1 # Positions in a list start from zero. To get correct index we should subtract one.

    # Determining the position of the first Quartile(q1).
    index1 = (len(numbers) + 1) // 4 # th position
    position1 = index1 - 1

    # Determining the position of the third quartile(q3).
    index2 = (3 * (len(numbers) + 1)) // 4 # th position.
    position2 = index2 - 1

    print("\nThe five number summary")
    print("-" * 30)
    print(f"Minimum: {minimum}")
    print(f"1st Quartile(q1): {numbers[int(position1)]}")
    print(f"Median(q2): {numbers[int(position)]}")
    print(f"3rd Quartile(q3): {numbers[int(position2)]}")
    print(f"Maximum: {maximum}")


def mean_calculator(numbers):
    # Mean calculation
    total = sum(numbers)# Finds the sum of the nuimbers on the list
    mean = total / len(numbers)# Calculation of the mean using formula from Stats

    print(f"\nMean: {mean}")

    return mean


def variance_standardDeviation_calc(numbers):
    mean = sum(numbers) / len(numbers)
    sumX2 = 0
    for number in numbers:
        sumX2 += number ** 2

    variance = (sumX2 - (len(numbers) * mean ** 2)) / (len(numbers) - 1)
    standard_deviation = variance ** 0.5

    print(f"Variance: {variance}")
    print(f"Standard deviation: {standard_deviation}")


def replace_item(numbers):
    old_item = int(input("Enter the number you want to replace: "))
    if old_item not in numbers:
        print("Number is not found in the list numbers")

    for i in range(len(numbers)):
        if numbers[i] == old_item:
            new_item = int(input("Enter the new number: "))
            index = numbers.index(old_item)
            numbers[i] = new_item

            numbers.sort()

            print("Number was replaced successfully.")


def display_data(numbers):
    print("Data:")
    print("*" * 10)
    for number in numbers:
        print(f"{number}")


def search(numbers):
    number = int(input("Enter numbe: "))
    if number not in numbers:
        print("Not Found!")
    for i in range(len(numbers)):
        if numbers[i] == number:
            print("found!")


def delete(numbers):
    number = int(input("Enter number: "))
    if number not in numbers:
        print("Number not found!")

    for i in range(len(numbers)):
        if numbers[i] == number:
            index = numbers.index(number)
            del numbers[index]
            print(f"The number {number} is deleted successfully...")


def Range_IQR(numbers):
    
    maximum = max(numbers)# Finds the maximum value from the list of numbers
    minimum = min(numbers)# Finds the minimum value from the list of numbers
     # Determining the position of the first Quartile(q1).
    index1 = (len(numbers) + 1) // 4 # th position
    position1 = index1 - 1

    # Determining the position of the third quartile(q3).
    index2 = (3 * (len(numbers) + 1)) // 4 # th position.
    position2 = index2 - 1

    Range = maximum - minimum
    IQR = numbers[int(position2)] - numbers[int(position1)]
    print("\nRange and IQR:")
    print(f"Range: {Range}")
    print(f"IQR: {IQR}")
    

def saving_items(numbers):
    try:
        with open("statistics.txt", "w") as outfile:
            for number in numbers:
                outfile.write(f"{number}\n")

            print("Items saved successfully...")

    except FileNotFoundError:
        print("The file was not found.")
    except IOError:
        print("Invalid input.")
    except Exception as error:
        print(error)


def main():
    numbers = []

    print("Statistical calculator v1")
    print("-" * 30)

    mean = None

    choice = ""

    while choice != "11":
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            numbers = add_elements()
        elif choice == "2":
            five_number_summary(numbers)

        elif choice == "3":
           mean = mean_calculator(numbers)

        elif choice == "4":
            variance_standardDeviation_calc(numbers)

        elif choice == "5":
            replace_item(numbers)

        elif choice == "6":
            saving_items(numbers)
        elif choice == "7":
            display_data(numbers)

        elif choice == "8":
            search(numbers)

        elif choice == "9":
            delete(numbers)

        elif choice == "10":
            Range_IQR(numbers)

        elif choice == "11":
            print("Thank you for using the calculator.")
            print("Goodbye...")


if __name__ == "__main__":
    main()
