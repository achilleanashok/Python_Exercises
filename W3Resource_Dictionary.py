#Ex 1: Write a Python program to sort (ascending and descending) a dictionary by value.

colors = {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4}


def dictionarry():
    key_value = {}

    # Initializing value
    key_value[2] = 56
    key_value[2] = 28
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print("Task 1:-\n")
    print("Keys are")

    for i in sorted(key_value):
        print((i, key_value[i]), end=" ")
    print("Task 2:-\n")
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))

    dictionary_of_names = {'beth': 37,
                           'jane': 32,
                           'john': 41,
                           'mike': 59
                           }

    print(dictionary_of_names)


def sort_dict_by_value(dictt, reverse = False):
    return dict(sorted(dictt.items(), key = lambda x: x[1], reverse=reverse))

def encode_string(sttt):
    dictt = {}

    for c in sttt:
        if c in dictt:
            dictt[c] += 1
        else:
            dictt[c] = 1
    print("".join(key, value) for key, value in dictt.items())
    return_str=""
    for key, value in dictt.items():
        return_str = return_str + key + str(value)
    print(return_str)
    return dictt

def main():
    #dictionarry()
    #print(sort_dict_by_value(colors, True))
    # d = {0:10, 1:20}
    # print(d)
    # d[2] = 30
    # d.update({3:40})
    # print(d)

    #Concatenate following dictionaries to create a new one

    # dict1 = {1:10, 2:20, 3:30}
    # dict2 = {4:40, 5:50, 6:60}
    # dict3 = {7:70, 8:80}
    # dict4 = {}
    # for d in (dict1, dict2, dict3):
    #     dict4.update(d)
    # print(dict4)


    #Ex5: Python program to check whether a given key already exists in a dictionary.
    encode_string("I am back.")


if __name__ == "__main__":
    main()