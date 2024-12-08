def kmp_search(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    lps = [0] * pattern_len 
    prefix_idx = 0
    
    for suffix_idx in range(1, pattern_len):
        while prefix_idx > 0 and pattern[suffix_idx] != pattern[prefix_idx]:
            prefix_idx = lps[prefix_idx - 1]
        if pattern[suffix_idx] == pattern[prefix_idx]:
            prefix_idx += 1
            lps[suffix_idx] = prefix_idx
    
    pattern_idx = 0
    match_count = 0
    match_positions = []
    
    for text_idx in range(text_len):
        while pattern_idx > 0 and text[text_idx] != pattern[pattern_idx]:
            pattern_idx = lps[pattern_idx - 1]
        if text[text_idx] == pattern[pattern_idx]:
            if pattern_idx == pattern_len - 1:
                match_count += 1
                match_positions.append(text_idx - pattern_len + 2)
                pattern_idx = lps[pattern_idx]
            else:
                pattern_idx += 1
    
    print(match_count)
    print(*match_positions)

input_text = input()
input_pattern = input()
kmp_search(input_text, input_pattern)
