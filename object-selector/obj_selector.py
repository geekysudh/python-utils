import json

def is_primitive(obj):
    return isinstance(obj, (int, float, bool, str)) 

def is_matching_primitive(lhs, rhs):
    if lhs == rhs:
        return True
    elif is_primitive(lhs) &  is_primitive(rhs):
        return str(lhs) == str(rhs)
    else:
        return False
 

def is_matching(obj:dict, criteria:dict):
    if obj == criteria:
        return True
    elif obj == None:
        return False
    else:
        keys = criteria.keys()
        matching = True 
        for key in keys:
            rhs = criteria.get(key)
            lhs = obj.get(key, None)
            if isinstance(rhs, dict):
                matching = matching & is_matching(lhs, rhs)
            else:
                matching = matching & is_matching_primitive(lhs, rhs)
            if not matching: 
                return matching    
        return matching


def select(obj_lists:list, criteria:dict):
    lst = []
    for x in obj_lists:
        if is_matching(x, criteria):
            lst.append(x)
    return lst

