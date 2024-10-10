# import builtins

# list=["a","b","c"]

# def print_dir_elements(obj_type):
#     methods_list = dir(obj_type)

#     for method in methods_list:
#         print(method)

# Example usage
# print_dir_elements(builtins)
# print(builtins.ZeroDivisionError.__doc__)


a = 10
b = 0
cloud_envs = ["aws","azure","gcp"]

try:
    print(cloud_envs[20]) #Whatever exception comes first only that one gets caught and the other one will get skipped
    c = a/b
    
except ZeroDivisionError as e: #Use as keyword to define exception object for multiple exceptions
    print("1",e)

except IndexError as e:
    print("2",e)