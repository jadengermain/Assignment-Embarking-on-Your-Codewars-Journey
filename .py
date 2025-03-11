def number_to_string(number):
    # Using str() function
    return str(number)

# Examples
print(number_to_string(123))  # Output: "123"
print(number_to_string(999))  # Output: "999"
print(number_to_string(-100)) # Output: "-100"

def remove_spaces(input_string):
    return input_string.replace(" ", "")

# Examples
print(remove_spaces("8 j 8   mBliB8g  imjB8B8  jl  B"))  # Output: "8j8mBliB8gimjB8B8jlB"
print(remove_spaces("8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd"))  # Output: "88Bifk8hB8BB8BBBB888chl8BhBfd"
print(remove_spaces("8aaaaa dddd r     "))  # Output: "8aaaaaddddr"

