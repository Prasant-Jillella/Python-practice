__author__ = 'PrasantJillella'
def dictionary_reed(dict):
    for k,v in dict.items():
        '''Cannot access the elements of dictionary directly must use item() function'''
        print(k,v)
dict={"prasant":1, "harikrishna":2, "tejarachakonda":3}
dictionary_reed(dict)