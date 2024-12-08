import sys
input = sys.stdin.readline


def compute_lps_array(pattern):
    length = len(pattern)
    lps = [0] * length
    k = 0

    for i in range(1, length):
        while k > 0 and pattern[i] != pattern[k]:
            k = lps[k - 1]

        if pattern[i] == pattern[k]:
            k += 1
            lps[i] = k

    return lps


def count_occurrences(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    lps = compute_lps_array(pattern)
    occurrence_count = 0

    i, k = 0, 0
    while i < text_len:
        if text[i] == pattern[k]:
            i += 1
            k += 1
        else:
            if k > 0:
                k = lps[k - 1]
            else:
                i += 1

        if k == pattern_len:
            occurrence_count += 1
            k = lps[k - 1]

    return occurrence_count


if __name__ == "__main__":
    n = int(input().strip())
    target_sequence = input().split()
    roulette_sequence = input().split()
    roulette_sequence += roulette_sequence[:-1]

    lps = compute_lps_array(target_sequence)
    match_count = count_occurrences(roulette_sequence, target_sequence)

    for gcd in range(match_count, 0, -1):
        if match_count % gcd == 0 and n % gcd == 0:
            print(f"{match_count // gcd}/{n // gcd}")
            break
