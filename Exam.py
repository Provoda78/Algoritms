def str_to_dict(s:str):
    res = {}
    l = s.split(':')
    
    for i in range(0, len(l), 2):
        key = l[i]
        
        if i+1 > len(l)-1:
            val = None
        else:
            val = l[i+1]
            
        if key in res:
            if isinstance(res[key], str):
                res[key] = [val, res[key]]
            else:
                res[key].append(val)
        else:
            res[key] = val
    
    return res

print(str_to_dict(input()))