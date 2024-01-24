def swap_case(s):
    invertedCaps=s.swapcase()
    return invertedCaps

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)