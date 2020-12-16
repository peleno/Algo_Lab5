radix = 128
# sufficiently large prime that does not overflow 2^32 when multiplied by radix
big_prime = 16777213

def compute_init_hash(text, pattern_length):
    hash_value = 0
    for i in range(pattern_length):
        hash_value = (hash_value * radix + ord(text[i])) % big_prime
    return hash_value

def compute_hash(pattern_length, prev_hash, new_char, old_char):
    h = radix ** (pattern_length -  1) % big_prime # radix to the power of m modulo big_prime
    return ((prev_hash - ord(old_char) * h) * radix + ord(new_char)) % big_prime

def check_match_naive(text, pattern, start_index):
    for i in range(len(pattern)):
        if pattern[i] != text[start_index + i]:
            return False
    return True

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
            if check_match_naive(text, pattern, i):
                indexes_of_matches.append(i)

    return indexes_of_matches

if __name__ == '__main__':
    text = "asdfaw efqawfasdfe"
    pattern = "w e"
    print(findAllMatches(text, pattern))