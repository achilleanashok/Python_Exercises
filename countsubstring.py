
def count_substring(mainstring, substring):
    cnt = 0
    for i in range(len(mainstring) - len(substring) + 1):
        print(mainstring[i:i+len(substring)])
        if mainstring[i:i+len(substring)] == substring:
            cnt += 1

    return cnt


string = "ABCDCDC"
substring = "CDC"
count_substring(string, substring)