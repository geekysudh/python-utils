import obj_selector
print("Hello")
  
# Defining main function
def main():
    data = []
    obj = {
        'name': 'Sudheesh',
        'age' : 20,
        'address':{
            'line1':'121212',
            'line2':'121212',
            'pin_code':'12345'
        }
    }
    data.append(obj)
    data.append({
        'name': 'Sudheesh1',
        'age' : 20,
        'address':{
            'line1':'121212',
            'line2':'121212',
            'pin_code':'12345'
        }
    })
    data.append({
        'name': 'Sudheesh1',
        'age' : 12,
        'address':{
            'line1':'121212',
            'line2':'121212',
            'line3':['121212'],
            'pin_code':'12.34'
        }
    })
    criteria0 = {
        'age' : 20,
    }
    obj_selector.select(data, criteria0);  
    criteria1 = {
        'address':{
            'pin_code':12.34,
        }
    }
    print(obj_selector.select(data, criteria1));  
    
# Using the special variable 
# __name__
if __name__=="__main__":
    main()