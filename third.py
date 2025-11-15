

#  Problem code
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
        return total  # Wrong indentation - returns after first iteration


#  correct code

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total  # Correct indentation - returns after loop completes

# Test the function
scores = [1, 2, 3, 4, 5]
result = calculate_sum(scores)
print(f"The sum of the numbers in the list {scores} is {result}")