binary = str(input())
bin_to_oct = ["000", "001", "010", "011", "100", "101", "110", "111"]
octal = []
len_bin = len(binary)
if len_bin % 3 == 2:
    binary = "0" + binary
elif len_bin % 3 == 1:
    binary = "00" + binary
len_bin = len(binary)

for i in range(0, len_bin, 3):
    octal.append("".join(binary[i:i + 3]))

for i in octal:
    for j in range(8):
        if i == bin_to_oct[j]:
            print(j, end = "")
            break
