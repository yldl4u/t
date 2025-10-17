def text_to_binary(text):
    """Converts a given string of text into its binary representation."""
    binary_representation = ' '.join(format(ord(char), '08b') for char in text)
    return binary_representation

def binary_to_text(binary_string):
    """Converts a given binary string into its text representation."""
    # Remove any spaces to handle different input formats
    binary_string = binary_string.replace(' ', '')
    
    # Split the binary string into 8-bit chunks
    text_representation = ""
    try:
        for i in range(0, len(binary_string), 8):
            byte = binary_string[i:i+8]
            if len(byte) == 8: # Ensure it's a full byte
                text_representation += chr(int(byte, 2))
            else:
                # Handle cases where the binary string isn't a perfect multiple of 8
                print(f"Warning: Incomplete byte found: {byte}. Skipping this part.")
    except ValueError:
        print("Error: Invalid binary string provided. Please ensure it only contains '0' and '1'.")
        return None
    return text_representation

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Text to Binary Converter ---")
    input_text = input("Enter text to convert to binary: ")
    binary_result = text_to_binary(input_text)
    print(f"Binary representation: {binary_result}")

    print("\n--- Binary to Text Converter ---")
    input_binary = input("Enter binary to convert to text (e.g., 01001000 01100101 01101100 01101100 01101111): ")
    text_result = binary_to_text(input_binary)
    if text_result is not None:
        print(f"Text representation: {text_result}")

    print("\n--- Let's try an example together! ---")
    sample_text = "Hello, GitHub!"
    print(f"Original Text: {sample_text}")
    
    sample_binary = text_to_binary(sample_text)
    print(f"Converted to Binary: {sample_binary}")
    
    decoded_text = binary_to_text(sample_binary)
    print(f"Decoded back to Text: {decoded_text}")
