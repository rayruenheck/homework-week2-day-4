# Write a function that takes two inputted lists of equal length and combines them into a single list by alternating elements. For example:
# Given list1 = [1, 2, 3] and list2 = ['a', 'b', 'c']
# The function should  return exactly this --->  [1, 'a', 2, 'b', 3, 'c'].





list_1 = [1,2,3]
list_2 = ['a','b','c']

def alternating_list(list_1, list_2):
    list_3 = []

    for i in range(len(list_1)):
        list_3.append(list_1[i])
        list_3.append(list_2[i])
    print(list_3)

alternating_list(list_1, list_2)