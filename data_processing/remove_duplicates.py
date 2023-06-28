def remove_duplicates(a_list):
    """
    Removes duplicates from a list.
    If the first element is a list, it flattens the list and removes duplicates.
    """

    res = []

    if type(a_list[0]) == list:
        res2= []
        [res.append(x) for x in a_list if x not in res for x in x]
        [res2.append(x) for x in res if x not in res2]
        return res2

    else:
        [res.append(x) for x in a_list if x not in res]

    return res
