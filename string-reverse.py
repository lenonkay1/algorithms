def reverse_string(input_string):
    if not input_string:
        return ""  
   
    reversed_str = ""
    for char in input_string:
        reversed_str = char + reversed_str
   
    return reversed_str


input_str = "Hello, World!"
reversed_result = reverse_string(input_str)
print("Original:", input_str)
print("Reversed:", reversed_result)
