import json
# Check if a given object is primitive or not
def is_primitive(obj):
    return isinstance(obj, (int, float, bool, str)) 

#Check if two objects are equal 
def equals(lhs, rhs):
    if lhs == rhs:
        return True
    elif is_primitive(lhs) &  is_primitive(rhs):
        return str(lhs) == str(rhs)
    elif isinstance(rhs, dict):
        return is_matching(lhs, rhs)
    else:
        return False

#Check if a given criteria is matching with supplied object 
def is_matching(obj:dict, criteria:dict):
    if obj == criteria:
        return True
    elif obj == None:
        return False
    else:
        keys = criteria.keys()
        matching = True 
        for key in keys:
            matching = matching & equals(obj.get(key, None), criteria.get(key))
            if not matching: 
                return matching    
        return matching

#Returns list of objects that matching the given criteria 
def select(obj_lists:list, criteria:dict):
    lst = []
    for x in obj_lists:
        if is_matching(x, criteria):
            lst.append(x)
    return lst

