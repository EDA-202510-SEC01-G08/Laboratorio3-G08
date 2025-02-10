def new_list():
    new_list = {"first": None,
                "last": None, 
                "size": 0,
                }
    return new_list

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    new_node = {"info": element,
                "next": None,
                }
    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        new_node["next"] = my_list["first"]
        my_list["first"] = new_node
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    new_node = {"info": element,
                "next": None,
                }
    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        my_list["last"]["next"] = new_node
        my_list["last"] = new_node
    my_list["size"] += 1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    return my_list["first"]

def remove_first(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    else:
        first = my_list["first"]
        now_first = first["next"]
        my_list["first"] = now_first
        my_list["size"] -= 1
        return first["info"]

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else: 
        return False
    
def last_element(my_list):
    last_element = my_list["last"]
    return last_element

def change_info(my_list, pos, new_info):
    if pos < 0 or pos > my_list["size"] -1:
        raise Exception('IndexError: list index out of range')
    else: 
        count = 0
        actual = my_list["first"]
        while actual != None and count != pos:
            count += 1
            actual = actual["next"]
        actual["info"] = new_info
        return actual


