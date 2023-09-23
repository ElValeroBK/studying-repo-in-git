my_string: str = "this is my str with hints"
my_string2 = "this is my str with hints2"

#print(type(my_string))


items: list[str] = ["lolo","lala"]

print(type(items))

### Type Hints ###

my_string_variable = "My String variable"
print(my_string_variable)
print(type(my_string_variable))

my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))

my_typed_variable: str = "My typed String variable"
print(my_typed_variable)
print(type(my_typed_variable))

my_typed_variable = 5
print(my_typed_variable)
print(type(my_typed_variable))

print(my_string.title())

def say_hi(name: str | None):
    print(f"Hey {name}!")

say_hi("")