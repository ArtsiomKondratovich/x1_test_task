def decoding(slug):
    res = []
    for i in slug:
        for ind, it in enumerate(CHAR):
            if i == it:
                res.append(ind)
            else:
                continue
    return sum(res)+1


CHAR = '0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
base = len(CHAR)
print(decoding('G'))
