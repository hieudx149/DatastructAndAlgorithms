def mergeSortArray(arr1, arr2):

    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    merge_array = []
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    i = 0
    j = 0
    arr1_item = arr1[i]
    arr2_item = arr2[j]
    while(i < len_arr1-1 or j < len_arr2-1):
        if arr1_item < arr2_item:
            merge_array.append(arr1_item)
            i += 1
            arr1_item = arr1[i]
        else:
            merge_array.append(arr2_item)
            j += 1
            arr2_item = arr2[j]
    return merge_array


if __name__ == '__main__':

    array1 = [5, 9, 10, 14]
    array2 = []
    print(mergeSortArray(array1, array2))