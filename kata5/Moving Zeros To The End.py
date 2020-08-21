def move_zeros(array):
    buffer = []
    zeroes = []
    for j, char in enumerate(array):
        if char == 0 and not isinstance(char, bool):
            zeroes.append(char)
        else:
            buffer.append(char)
    return buffer + zeroes
# https://www.codewars.com/kata/52597aa56021e91c93000cb0
