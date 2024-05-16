def decrypt_line(encrypted_line, key_sentence):
    key_sentence = key_sentence.replace(' ', '')
    encrypted_line = encrypted_line.replace(' ', '')
    if len(encrypted_line) != len(key_sentence):
        return None
    
    key_map = {}
    for encrypted_char, key_char in zip(encrypted_line, key_sentence):
        if encrypted_char not in key_map:
            key_map[encrypted_char] = key_char
        elif key_map[encrypted_char] != key_char:
            return None
    
    decrypted_line = ''.join([key_map[char] for char in encrypted_line])
    return decrypted_line

# Sample input
encrypted_lines = [
    "recomtiatonahedsllfeeunarteyenatetiasouehtiawsdtg",
    "aotsirhdlneucmefyiwgpebtnaotvkxqjez",
    "denseirrltsuntaohahieocmtieotaafoy"
]
known_plaintext = "the quick brown fox jumps over the lazy dog"

# Decrypt each line
for encrypted_line in encrypted_lines:
    decrypted_line = decrypt_line(encrypted_line, known_plaintext)
    if decrypted_line:
        print(decrypted_line)
    else:
        print("No solution.")
