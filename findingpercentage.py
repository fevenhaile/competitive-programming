if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    values_of_query=student_marks[query_name]
    
    print(format(sum(values_of_query)/3,'.2f'))
    