#Архиватор методом RLE

def encode(line):

    if len(line) < 2:
        return line

    encoded_line = line[0]    
    i = 1

    while i < len(line):
        
        encoded_line += line[i]
        if line[i] == line[i - 1]:
            subseq_len = 0
            i += 1
            while i < len(line) and subseq_len < 15 and line[i] == line[i - 1]:
                subseq_len += 1
                i += 1
            encoded_line += hex(subseq_len)[-1]
        else:
            i += 1

    return encoded_line

def decode(line):

    if len(line) < 2:
        return line

    decoded_line = line[0]
    i = 1

    while i < len(line):

        decoded_line += line[i]
        if decoded_line[-1] == decoded_line[-2]:
            i += 1
            subseq_len = int('0x' + line[i], base = 16)
            decoded_line += decoded_line[-1]*subseq_len

        i += 1

    return decoded_line
    
        
input_name = input('Введите имя входного файла: ')
output_name = input('Введите имя выходного файла: ')
compress_mode = int(input('Введите режим работы: 0 - разархивация файла, любое другое число - архивирование: '))

with open(input_name) as input_file:
    with open(output_name, mode = 'w') as output_file:
        for input_line in input_file:
            output_line = encode(input_line) if compress_mode else decode(input_line)
            output_file.write(output_line)
    
           
