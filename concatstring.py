
def concat_mid(s1, s2):
    len_s1 = len((s1.strip()))
    mid = int(len_s1/2)
    if len_s1 == 0:
        return s2
    elif len_s1 == 1:
        return s1 + s2
    else:
        return s1.strip()[:mid] + s2 + s1[mid+1:]


print(concat_mid("   something123","great"))