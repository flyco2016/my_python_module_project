# 处理嵌套的根据键取值

def getItemByKey(obj, key, result=None):
    if isinstance(obj, dict):
        for k in obj:
            if key == k:
                if isinstance(result, list):
                    if isinstance(obj[k], list):
                        result.extend(obj[k])
                    else:
                        result.append(obj[k])
                elif result is None:
                    result = obj[k]
                else:
                    result = [result]
                    result.append(obj[k])
            else:
                if isinstance(obj[k], dict) or isinstance(obj[k], list):
                    result = getItemByKey(obj[k], key, result)
    elif isinstance(obj, list):
        for i in obj:
            if isinstance(i, dict) or isinstance(i, list):
                result = getItemByKey(i, key, result)
    return result[0] if isinstance(result, list) and len(result) == 1 else result

def getItemByKeyInMyMethod(dict_obj, key, default=None):
    import types
    for k ,v in dict_obj.items():
        if k == key:
            return v
        else:
            if type(v) is dict:
                ret = getItemByKeyInMyMethod(v, key, default)
                if ret is not default:
                    return ret
    return default


if __name__ == "__main__":
    test_dic = {'a': 1, 'b': 2, 'c': {'a': 1, 'b': {'b': 4}}}
    r1 = getItemByKey(test_dic, 'b')
    r2 = getItemByKeyInMyMethod(test_dic, 'b')

    print(r1, r2, sep='\n')