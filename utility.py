
def find_max(numbers):
    maximus = numbers[0]
    for number in numbers:

        if number > maximus:
            maximus=number
    return maximus


