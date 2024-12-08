while True:
    data = input()
    if data == ".":
        break

    length = len(data)
    lps = [0] * length
    match_length = 0

    for index in range(1, length):
        while match_length > 0 and data[index] != data[match_length]:
            match_length = lps[match_length - 1]
        if data[index] == data[match_length]:
            match_length += 1
            lps[index] = match_length

    unit_length = length - lps[-1]  
    result = length // unit_length if length % unit_length == 0 else 1
    print(result)
