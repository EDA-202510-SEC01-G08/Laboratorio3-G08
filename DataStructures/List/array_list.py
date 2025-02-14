def new_list():
    new_list = {"elements": [],
                "size": 0,
                }
    return new_list

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    return my_list["elements"][0]

def is_empty(my_list):
    return my_list["size"] == 0

def get_fist_element(my_list):
    return my_list["elements"][0]

def insert_element(my_list, element, index):
    my_list["elements"].insert(index, element)
    my_list["size"] += 1
    return my_list
def delete_element(my_list, index):
    if my_list["size"] > 0:
        my_list["elements"].pop(index)
        my_list["size"] -= 1
    return my_list
def change_info(my_list, index, element):
    my_list["elements"][index] = element
    return my_list
def exchange(my_list, pos1, pos2):
    temp = my_list["elements"][pos1]
    my_list["elements"][pos1] = my_list["elements"][pos2]
    my_list["elements"][pos2] = temp
    return my_list

def sub_list(my_list, start, end):
    sublist = new_list()
    for i in range(start, end):
        add_last(sublist, my_list["elements"][i])
    return sublist

def remove_last(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    else: 
        elementos = my_list["elements"]
        size = my_list["size"]
        elemento = elementos[size-1]
        del elementos[size-1]
        my_list["size"] -= 1
        return elemento
    
def remove_first(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    else: 
        elementos = my_list["elements"]
        elemento = elementos[0]
        del elementos[0]
        return elemento