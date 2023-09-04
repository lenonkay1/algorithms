def find_largest_smallest(numbers):
    if not numbers:
        return None, None
   
    largest = smallest = numbers[0]
   
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
           
    return largest, smallest


input_list = [12, 5, 7, 18, 11, 6, 4, 17, 3, 9]
largest_num, smallest_num = find_largest_smallest(input_list)
print("Largest:", largest_num)
print("Smallest:", smallest_num)
