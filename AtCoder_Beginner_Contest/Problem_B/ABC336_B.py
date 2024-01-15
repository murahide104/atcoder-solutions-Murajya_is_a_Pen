def decimal_to_binary(decimal_number):
    binary_representation = bin(decimal_number)
    return binary_representation[2:]

n = int(input())
binary_number = str(decimal_to_binary(n))[::-1]

cnt = 0
for n in binary_number:
    if n == "0":
        cnt += 1
    else:
        break

print(cnt)