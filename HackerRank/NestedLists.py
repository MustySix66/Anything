if __name__ == '__main__':
    listaexterior = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        listaexterior.append([name, score])
second_highest = sorted(set([score for name, score in listaexterior]))[1]
print('\n'.join(sorted([name for name, score in listaexterior if score == second_highest])))