

def split_and_join(string):
    S = string.split()
    J = '-'.join(S)
    return J

if __name__ == '__main__':
    string = input()
    result = split_and_join(string)
    print(result)