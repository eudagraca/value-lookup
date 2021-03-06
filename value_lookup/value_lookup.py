"""
    :pivot_value: Value to check in list
    :the_list: list where you will search for the value
    :complete_analysis: Conditioning of the return value (if true, the return value will give more details like size, object type, found values)
"""

def vlookup(pivot_value, the_list, complete_analysis=False):
    result= []
    counter = 0
    list_of: None

    #convert integer list  to string list
    if isinstance(the_list, list):
        list_of = map(str, the_list)
    else:
        list_of = str(the_list)

    for value in list_of:
        if str(pivot_value) == value:
            result.append(value)
            counter += 1
    
    if  complete_analysis:
        return {'founded_values': result, 
                'size_of_returned_list': counter,  
                'object_type': type(result)
            }
    else:
        return bool(result)