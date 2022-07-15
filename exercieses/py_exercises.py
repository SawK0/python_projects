
# find missing number
def find_missing_number(num_list):
    return set(range(len(num_list)+1)) - set(num_list)


x = list(range(100))
print(x[::2])
