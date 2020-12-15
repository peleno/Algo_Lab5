radix = 128

def compute_init_hash(text, pattern_length):
    hash_value = 0
    for i in range(pattern_length):
        hash_value = hash_value * radix + ord(text[i])
    return hash_value

def compute_hash(pattern_length, prev_hash, new_char, old_char):
    return (prev_hash - ord(old_char) * radix ** (pattern_length - 1)) * radix + ord(new_char)

def findAllMatches(text, pattern):
    n = len(text)
    m = len(pattern)
    pattern_hash = compute_init_hash(pattern, m)
    current_hash = compute_init_hash(text, m)
    indexes_of_matches = []
    if current_hash == pattern_hash:
        indexes_of_matches.append(0)
    for i in range(1, n - m + 1):
        current_hash = compute_hash(m, current_hash, text[i + m - 1], text[i - 1])
        if current_hash == pattern_hash:
            indexes_of_matches.append(i)

    return indexes_of_matches

if __name__ == '__main__':
    text = "asdfaw efqawfasdfe"
    pattern = "w e"
    print(findAllMatches(text, pattern))