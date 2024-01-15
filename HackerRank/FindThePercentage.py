if __name__ == '__main__':
    ## Number of students
    n = int(input("n: "))
    ## We create a list
    student_marks = {}
    for i in range(n):
        name, *line = input("name, *line: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("query name: ")
    l1 = list(student_marks[query_name]) 
    addition = sum(l1)
    result = addition/len(l1)
    print('%.2f'% result)

    ## these next print are just to check the input data hosted in the list and the dictionary
    ## Need to remove it to get the problem solved.
    print(scores)
    print(student_marks)

