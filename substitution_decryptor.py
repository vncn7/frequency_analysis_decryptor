from collections import Counter

# Frequency of each letter in the English and German language
sorted_letter_percentages_english = {
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97,
    'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25,
    'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36,
    'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29,
    'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10,
    'Z': 0.07
}

# Clean the text by removing all non-alphabetic characters and converting it to uppercase
def clean_text(text):
    return ''.join(filter(str.isalpha, text.upper()))

# Calculate the percentage of each letter in the text and sort them in descending order
def calculate_letter_percentages(text):
    letter_frequencies = Counter(text)
    sorted_letter_percentages = {letter: (count / len(text) * 100) for letter, count in sorted(letter_frequencies.items(), key=lambda item: item[1], reverse=True)}
    return sorted_letter_percentages

# Decrypt the text using the frequency analysis technique
def decrypt(encrypted_text, shifts = 10):
    cleaned_text = clean_text(encrypted_text)
    encrypted_letter_percentages = calculate_letter_percentages(cleaned_text)

    # multiple shifts 
    # different combinations. biagrams and tri-grams maybe? try multiple stuff and print everyone.
    # alaso implement 
    print(sorted_letter_percentages_english)
    print(encrypted_letter_percentages)

    # temp
    decrypted_text = ""
    
    return decrypted_text

def main():
    encrypted_text = "LFAJ AJ LFO JADNKO OHECUNLAWH WY Q JADNKO LOML ALJ ZOLLOC LW FQTO KWTOB QHB KWJL LFQH HOTOC LW FQTO KWTOB QL QKK"
    
    # test functions
    decrypted_text = decrypt(encrypted_text)



    print("\nOriginal encrypted text:")
    print(encrypted_text)
    print("\nDecrypted text:")
    print(decrypted_text)

if __name__ == "__main__":
    main()