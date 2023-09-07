def analyze_string(input_string):
    num_alphabets = num_digits = num_symbols = num_uppercase = num_lowercase = 0

    for char in input_string:
        if char.isalpha():
            num_alphabets += 1
            if char.isupper():
                num_uppercase += 1
            elif char.islower():
                num_lowercase += 1
        elif char.isdigit():
            num_digits += 1
        else:
            num_symbols += 1

    return num_alphabets, num_digits, num_symbols, num_uppercase, num_lowercase

def main():
    input_string = input("Enter a string: ")
    num_alphabets, num_digits, num_symbols, num_uppercase, num_lowercase = analyze_string(input_string)

    print("Number of Alphabets:", num_alphabets)
    print("Number of Digits:", num_digits)
    print("Number of Symbols:", num_symbols)
    print("Number of Uppercase Alphabets:", num_uppercase)
    print("Number of Lowercase Alphabets:", num_lowercase)

if __name__ == "__main__":
    main()