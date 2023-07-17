
### which one do you prefer

def check_positive(list):
    positive_element = []
    for element in list:
        if element > 0:
            positive_element.append(element)
    return positive_element



def check_positive_single_line(list):
    return [element for element in list if element > 0]

list_1 = [-1,1,-3,4,5,7,6,-4,-5,-6,-7]
print(check_positive(list_1))
print(check_positive_single_line(list_1))