def string_reverse(str1):
    rstr = ''
    index = len(str1)
    while index>0:
        rstr1 += str1[index-1]
        index = index-1
    return str1
print(string_reverse('1234abcd'))
