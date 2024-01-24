def mutate_string(string, position, character):
    original=string
    posi=position
    newLetter=character

    l = list(original)
    l[posi] = newLetter
    olabb = ''.join(l)
    
    return olabb

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)