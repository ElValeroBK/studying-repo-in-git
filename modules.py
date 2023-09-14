#import utility    # one way to call a module
#utility.find_max()



from utility import find_max   #second way to call module
numbers = [2,8,75,3,50,1]
maximus=find_max(numbers)
print(maximus)