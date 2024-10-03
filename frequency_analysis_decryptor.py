from collections import Counter

# The encrypted text
encrypted_text = "LFAJ AJ LFO JADNKO OHECUNLAWH WY Q JADNKO LOML ALJ ZOLLOC LW FQTO KWTOB QHB KWJL LFQH HOTOC LW FQTO KWTOB QL QKK"

# Remove non-alphabetic characters (e.g., spaces) for frequency analysis
cleaned_text = ''.join(filter(str.isalpha, encrypted_text))

# Frequency analysis
letter_frequencies = Counter(cleaned_text)
print(letter_frequencies)

