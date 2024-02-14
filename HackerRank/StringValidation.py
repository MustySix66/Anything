if __name__ == '__main__':
    s = input()
    Alpha = any(char.isalnum() for char in s)
    alfa = any(char.isalpha() for char in s)
    Mayus = any(char.isupper() for char in s)
    Minus = any(char.islower() for char in s)
    Nums = any(char.isdigit() for char in s)

    print(Alpha) #  alphanumeric characters.
    print(alfa) #  alphabetical characters.
    print(Nums) # digits
    print(Minus) #  lowercase characters.
    print(Mayus)
