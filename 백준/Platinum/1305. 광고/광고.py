import sys


def create_table(pattern):
    pattern_length = len(pattern)
    lps = [0] * pattern_length
    prefix_index = 0
    for current_index in range(1, pattern_length):
        while prefix_index > 0 and pattern[current_index] != pattern[prefix_index]:
            prefix_index = lps[prefix_index - 1]
        if pattern[current_index] == pattern[prefix_index]:
            prefix_index += 1
            lps[current_index] = prefix_index
    return lps


length = int(sys.stdin.readline())
text = sys.stdin.readline().rstrip()

print(length - create_table(text)[-1])
