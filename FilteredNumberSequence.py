from itertools import product
file = open("TheFunnyNumbers.txt", "w")
def generate_combinations(digits, length):
    # Generate all combinations of the given digits and length
    combinations = product(digits, repeat=length)
    for combo in combinations:  
        print("".join(map(str, combo)))
        file.write(str("".join(map(str, combo))) + "\n") 

# Parameters: allowed digits and number of digits

number_of_digits = int(input("Enter the number of digits you want to generate: "))
allowed_digits = list(range(1, number_of_digits + 1))


# Generate and print all combinations
generate_combinations(allowed_digits, number_of_digits)

file.close()