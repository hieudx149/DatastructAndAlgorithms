def revertString1(string):
    my_list = []
    for i in range(len(string)-1, -1, -1):
        my_list.append(string[i])
    return ''.join(my_list)

def revertString2(string):
    return ''.join(reversed(string))

my_string = 'xuan hieu'

if __name__ == '__main__':
    print(revertString2(my_string))