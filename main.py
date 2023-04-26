# 1

def selection_sort(numbers: list):
    for fill_slot in range(len(numbers)-1, 0, -1):
        position_of_max = 0
        for location in range(1, fill_slot + 1):
            if numbers[location] > numbers[position_of_max]:
                position_of_max = location
        temp = numbers[fill_slot]
        numbers[fill_slot] = numbers[position_of_max]
        numbers[position_of_max] = temp


# Comment
random_list = [4, 2, 1, 6, 7, 8, 3, 5]
print(f"random list before sorting: {random_list}")
selection_sort(random_list)
print(f"random list after sorting: {random_list}")
