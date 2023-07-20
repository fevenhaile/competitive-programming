def new(c):
    if str.isupper(c):
      return str.lower(c)
    else:
        return str.upper(c)


def swap_case(s):
    return "".join(map(new,s))
  

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)