# for i in range(3):
#     for j in range(2):
#         print(i, j)

data = [
    {'name': 'Alice', 'location': 'New York', 'link': 'http://example.com/alice'},
    {'name': 'Bob', 'location': 'Los Angeles', 'link': 'http://example.com/bob'},
    {'name': 'Charlie', 'location': 'Chicago', 'link': 'http://example.com/charlie'}
]

#print(type(data))
print(enumerate(data))
for x in data:
    print(x)

print("\n")

print(range(len(data)))
print("\n")
print(range(data))
# for a, b in data.items():
#     print(a, b)

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(type(my_dict))
# for key, value in my_dict.items():
#     print(key, value)

# for i, row in enumerate(data):
#     if i >= last_populated_line:
#         writer.writerow(row)