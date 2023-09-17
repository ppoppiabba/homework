
def rev_str(s):
    if len(s) == 0:
        return ""
    
    return s[-1] + rev_str(s[:-1])

if __name__ == '__main__':
    print(rev_str('ABCDE'))
    print(rev_str('Come again, Forever young!'))
    print(rev_str('Amore, Roma'))
