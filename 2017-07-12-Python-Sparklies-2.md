**''.format()**
def sloganify(x):
    return "{} or bust!".format(x)

**inspect**
>>> import inspect
>>> inspect.signature(bar_function)
<Signature (x, y, z)>

dictionary.get (d.get) ?
def generatezipName(zipcode_org_number):
    return [sources.neighboorhood_names.get(int(z), "None") for z in zipcode_org_number]
This example also uses get instead of brackets for the dict lookup, which doesn't throw an exception if the key is not found. The 2nd argument here is the value returned if the key isn't found, so it produces the exact same results as your original fn.

that cool memoization thing Ramalho talked about - maybe a decorator??
