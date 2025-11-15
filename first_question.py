
def filter_uniqueitems(numbers):
    seen = set()
    unique_list = []
    for num in numbers:
        if num not in seen:   # check if number is new
            unique_list.append(num)
            seen.add(num)     # mark it as seen
    return unique_list


# Example usage
numbers = [1,2,3,4,5,6,1,2,3,4,5,6,7,8,9]
print(filter_uniqueitems(numbers))
