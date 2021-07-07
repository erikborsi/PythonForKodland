# A list of integers is given. It is required to "shrink" it by moving all non-zero elements to the left side of the
# list without changing their order, and all zeros to the right side.
# The order of the non-zero elements cannot be changed, an additional list cannot be used, and the task must be
# completed in one pass through the list. Print the resulting list.
#
# Example input data:
# 4 0 5 0 3 0 0 5
#
# Example result:
# 4 5 3 5 0 0 0 0

list_original = [4, 0, 5, 0, 3, 0, 0, 5]
list_temp = []

def remove_zero_to_temp_list(list_in):
    for i in list_in:
        if i == 0:
            list_temp.append(i)

    for i in list_in:
        if i == 0:
            list_in.remove(i)
            for j in list_in:
                if j == 0:
                    list_in.remove(j)

def merge_two_lists(list_one, list_two):
    for i in list_two:
        list_one.append(i)
    list_two.clear()


remove_zero_to_temp_list(list_original)
merge_two_lists(list_original, list_temp)

print(list_original)
