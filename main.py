def flatten_list(l):
    flat_list = []
    for sublist in l:
        if type(sublist) == list:
            flat_list.extend(flatten_list(sublist))
        else:
            flat_list.append(sublist)
    return flat_list

