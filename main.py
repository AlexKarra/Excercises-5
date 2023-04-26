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


# Comment N1
random_list = [4, 2, 1, 6, 7, 8, 3, 5]
print(f"random list before sorting: {random_list}")
selection_sort(random_list)
print(f"random list after sorting: {random_list}")



# 2

def binary_search(text: list, target: str) -> str:
    first = 0
    last = len(text) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if text[mid] == target:
            found = True
        else:
            if target < text[mid]:
                last = mid - 1
            else:
                first = mid + 1

    if found:
        return text[mid]
    else:
        return "Target string not found in the list"

# Comment N2
text = ['T-shirts', 'Jeans', 'Coats', 'Hats', 'Underwear', 'Accessories']
target = 'Underwear'

result = binary_search(text, target)
print(f"Result: {result}")




# 3 - 6

class HashTable:
    def _init_(self, size):
        self.size = size
        self.table = [[] for n in range(size)]

    def __my_hash(self, key):
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            hash_value = 0
            for char in key:
                hash_value = (hash_value * 31 + ord(char)) % self.size
            return hash_value
        else:
            raise TypeError(f"Unsupported key type: {type(key)}")

    def put(self, key, data):
        hash_value = self.__my_hash(key)
        bucket = self.table[hash_value]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, data)
                return
        bucket.append((key, data))

    def get(self, key):
        hash_value = self.__my_hash(key)
        bucket = self.table[hash_value]
        for k, v in bucket:
            if k == key:
                return v                # return the value only, not the key
        return None  # return None if key is not found
    
# Comment N3
table = HashTable(10)
table.put('Alice', 25)
table.put('Bob', 32)
table.put('Charlie', 19)
print(table.get('Alice'))
print(table.get('Bob'))
print(table.get('Charlie'))
