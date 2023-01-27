def flatten_list(l):
    new_list = []
    for i in l:
        new_list+=i
    x = "["
    for i in new_list:
        x+=str(i)
        x+=","
    x = x[:-1]+"]"
    return x
