
#complexity O(1)
def frist_recurring_character(arrary):
    map_arr = {} # if here we use a list --> O(n)

    for item in arrary:
        if item in map_arr: # O(1)
            return item
        else:
            map_arr[item] = 0 # just equal anything
    return None

my_arr = [1,2,2,4,4,1,6]
print(frist_recurring_character(my_arr))