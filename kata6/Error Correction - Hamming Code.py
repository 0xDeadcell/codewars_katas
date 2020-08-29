from sys import argv

def encode(string):
    bits = "".join([ f'{ord(letter):>08b}' for letter in string ])
    bits = bits.replace("0", "000")
    bits = bits.replace("1", "111")
    return bits

def decode(bits):
    chunked_bits = [ bits[x:x+3] for x in range(0, len(bits), 3)]
    validated_bits = []
    for group in chunked_bits:
        if group.count('1') >= 2:
            validated_bits.append('1')
        else:
            validated_bits.append('0')
    validated_bits = "".join(validated_bits)
    binary_letters = [ "".join(validated_bits[x:x+8]) for x in range(0, len(validated_bits), 8) ]
    string = "".join([ chr(int(b, 2)) for b in binary_letters ])
    
    return string

if __name__ == "__main__":
    if argv[1].lower() == 'encode':
        ascii_data = " ".join(argv[2:])
        print(ascii_data, "-->", encode(ascii_data), sep=" ")
    elif argv[1].lower() == 'decode':
        bin_data = " ".join(argv[2:])
        print(bin_data, "-->", decode(bin_data), sep=" ")
