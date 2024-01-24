def split_and_join(line):
    line = line.strip() ## retira los espacios del inicio y de el final
    line = line.split() ## separa las palabras en distintas string
    joined="-".join(line) ## une las palabras en una sola cadena por medio del caracter seleccionado.
    return joined

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)