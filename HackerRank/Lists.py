if __name__ == '__main__':
    N = int(input())
    ListaMamalona=[];
    for i in range(N):
        command=input().split();
        if command[0] == "insert":
            ListaMamalona.insert(int(command[1]),int(command[2]))
        elif command[0] == "append":
            ListaMamalona.append(int(command[1]))
        elif command[0] == "pop":
            ListaMamalona.pop();
        elif command[0] == "print":
            print(ListaMamalona)
        elif command[0] == "remove":
            ListaMamalona.remove(int(command[1]))
        elif command[0] == "sort":
            ListaMamalona.sort();
        else:
            ListaMamalona.reverse();

