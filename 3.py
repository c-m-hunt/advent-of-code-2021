def find_most_frequent_bits(bit_list):
    how_many = len(bit_list)
    counter = [0] * len(bit_list[0])

    for bits in bit_list:
      for i, bit in enumerate(bits):
        if bit == '1':
          counter[i] += 1
    gamma = ''
    epsilon = ''
    for count in counter:
        gamma += '1' if count >= how_many/2 else '0'
        epsilon += '0' if count >= how_many/2 else '1'

    return(gamma, epsilon)

def get_ogr(bit_list):
    for i in range(len(bit_list[0])):
        gamma, epsilon = find_most_frequent_bits(bit_list)
        bit_list = filter_bit(bit_list, i, gamma)
        if len(bit_list) == 1:
            return bit_list
    return bit_list

def get_co2s(bit_list):
    for i in range(len(bit_list[0])):
        gamma, epsilon = find_most_frequent_bits(bit_list)
        bit_list = filter_bit(bit_list, i, epsilon)
        if len(bit_list) == 1:
            return bit_list
    return bit_list

def filter_bit(bit_list, i, mask):
    new_bit_list = []
    for j, bits in enumerate(bit_list):
        if mask[i] == bits[i]:
            new_bit_list.append(bits)
    return new_bit_list
      

filename = "./input/3.txt"
with open(filename) as file:
    lines = file.readlines()
    lines = [list(line.rstrip()) for line in lines]


gamma, epsilon = find_most_frequent_bits(lines)
print(gamma, epsilon)
print(int(gamma, 2), int(epsilon, 2))
print("Power: ", int(gamma, 2) * int(epsilon, 2))

ogr = get_ogr(lines)
co2s = get_co2s(lines)

print(ogr, co2s)
print(len(ogr), len(co2s))
print(int("".join(ogr[0]), 2), int("".join(co2s[0]), 2))
print("Life support rating: ", int("".join(ogr[0]), 2) * int("".join(co2s[0]), 2))