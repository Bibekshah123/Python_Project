# smallest = None
# print("Before:", smallest)
# for itervar in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#         break
#     print("Loop:", itervar, smallest)
# print("Smallest:", smallest)

# print('before')
# for value in [1, 3, 5, 6, 8, 39]:
#     if value > 3:
#         print("large number",value)
#     print("after")

# smallest_num = 30
# for num in [2, 6, 89, 45, 67, 90]:
#     if num < smallest_num:
#         print("smallest num is", num)
#         smallest_num = num

# thislist = (("apple", "banana", "cherry"))
# print(type(thislist))

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = [ "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")
# else:
#     print("No, apple isn't int the list")


# item = ["a", "b", "c"]
# item[2] = "d"
# print(item)

# list = ["a", "b", "c", "d"]
# list.append("e")
# print(list)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove( "banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

car = {
  'brand' : 'lambo',
  'model' : 'mustang',
  'year' : 2023
}

x = car.values()
print(x)

car['year'] = 2020

print(x)