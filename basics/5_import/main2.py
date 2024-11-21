print("1. Import module... Should be a module and contain ALL submodules")

import module
import module.fancy_class

print(module)

print("2. Try to use the fancy class --- should be a module.")

print(module.fancy_class)

print('Notice what just happened: VSCode *automatically* imported the fancy class.')
