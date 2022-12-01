

def reverse(arg:list) -> list:
    new_list = list()
    length = len(arg)
    for _ in arg:
        new_list.append(arg[length - 1])
        length = length - 1
    return new_list   


def insert(arg:list , value, index:int) -> list:
    new_list = list()
    
    
    new_list.extend(arg[:index:])
    new_list.append(value)
    return new_list
    
            

if __name__ == "__main__":
                
    print(insert([item for item in range(100)], "aryan", 10))
        