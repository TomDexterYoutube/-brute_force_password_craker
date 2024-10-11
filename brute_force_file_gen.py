import random
import string
from tqdm import tqdm  # Ensure to install tqdm using pip if not already installed

# Function to generate unique random strings
def generate_random_strings(num_strings, length, use_upper, use_lower, use_digits, use_special, filename):
    # Create a character pool based on user selection
    char_pool = ''
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation  # Adding special characters

    # Check if the character pool is not empty
    if not char_pool:
        print("No character types selected. Please enable at least one type of character.")
        return

    # Set to store generated strings for uniqueness
    generated_strings = set()

    # Open the file for appending with error handling
    try:
        with open(filename, "a") as file:
            while len(generated_strings) < num_strings:
                text = ''.join(random.choices(char_pool, k=length))
                # Check if the string is unique
                if text not in generated_strings:
                    generated_strings.add(text)  # Add unique string to the set
                    file.write(text + "\n")  # Write the string followed by a newline
                # Progress bar updates
                tqdm.write(f"Generated {len(generated_strings)} unique strings...", end='\r')

    except IOError:
        print("An error occurred while trying to write to the file.")

# Main execution block
if __name__ == "__main__":
    try:
        count = int(input("Enter the number of random strings to generate: "))  # Get user input for count
        if count < 1:
            print("Please enter a positive integer.")
            exit()
        
        string_length = int(input("Enter the length of each random string: "))  # Get user input for string length
        if string_length < 1:
            print("Please enter a positive integer for the string length.")
            exit()

        # User input for character types
        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
        
        # Get custom filename from user
        filename = input("Enter the filename to save the strings (default is 'data.txt'): ") or "data.txt"

        generate_random_strings(count, string_length, use_upper, use_lower, use_digits, use_special, filename)
        print(f"\n{count} unique random strings of length {string_length} have been saved to '{filename}'.")

    except ValueError:
        print("Invalid input! Please enter valid integers.")
