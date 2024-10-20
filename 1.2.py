def generate_password(n):
    result = ""
    used_pairs = set()
    for i in range(1, n):
        for j in range(i+1, n+1):
            pair_sum = i + j
            if pair_sum <= n and n % pair_sum == 0:
                if (i, j) not in used_pairs and (j, i) not in used_pairs:
                    result += str(i) + str(j)
                    used_pairs.add((i, j))
    return result
for n in range(3, 21):
    password = generate_password(n)
    print(f"{n} - {password}")