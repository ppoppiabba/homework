remainders = [int(input("숫자 입력: ")) % 42 for _ in range(10)]

unique_remainders = len(set(remainders))

print(unique_remainders)
