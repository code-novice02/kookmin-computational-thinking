octal = str(input())
oct_to_bin = ["000", "001", "010", "011", "100", "101", "110", "111"]
list_binary = []
for i in octal:
    list_binary.append(oct_to_bin[int(i)])
binary = "".join(list_binary)

strip_zero_binary = binary.lstrip('0')

if strip_zero_binary == "":
    print("0")
else:
    print(strip_zero_binary)
