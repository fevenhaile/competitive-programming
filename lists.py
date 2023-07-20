if __name__ == '__main__':
    N = int(input())
    list=[]
    for items in range (N ):
        cmd = input().split()
        if cmd[0] == 'insert':
            list.insert(int(cmd[1]),int(cmd[2]))
        if cmd[0] == 'print':
            print(list)
        if cmd[0] == 'remove':
                list.remove(int(cmd[1]))
        if cmd[0] == 'append':
                list.append(int(cmd[1]))
        if cmd[0] == 'sort':
                list.sort()
        if cmd[0] == 'pop':
                list.pop()
        if cmd[0] == 'reverse':
                list.reverse()
        
        
