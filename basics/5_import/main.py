import module
import module.sub_module
import module.sub_module.subcomputation

print("Should be a module:")
print(module)

print("Should be a module:")
print(module.computation)

print("Should be a function:")
print(module.addition)

print("Should be a float:")
print(module.addition(26.5235, 2352.534))

print("Should be a (sub)module")
print(module.sub_module)

print("Should be a submodule")
print(module.sub_module.subcomputation)

print("Should be a function:")
print(module.sub_module.subaddition)

print("Looks like all the 'subcalls' get automatically added by VSCode...")
print("And the above will NOT work unless it's exposed through the __init__.py file")