#names = "Python"
# #scores = [95, 87, 92]
# #tags = ["Python", "AI", "Beginner"]
# #print(names[1])
# #print(scores[1])
# #print(tags[1])
# #lists maintain order and sets do not maintain order

# #names = "Python"
# #scores = [95, 87, 92]
# #tags = {"Python", "AI", "Beginner"}
# #print(names[1])
# #print(scores[1])
# #print(tags)

# #s = "hello"
# #s[0] = "H"
# #print(s)


# # print(type({})) # ________
# # print(type(set())) # ________


# # lst = [10, 20, 30]
# # lst[0] = 99
# # print(lst)

# # print({1, 2, 2, 3, 3, 3})
# # print([1, 2, 2, 3, 3, 3])


# # s = {1, 2, 3}
# # s.add(42)
# # s.add("hello")
# # s.add((10, 20))
# # # s.add([1, 2])  # This will cause a TypeError, 

# # print(hash((1, 2, 3))) # ________ (works)
# # #print(hash((1, [2, 3]))) # ________ (what happens?)

# # print('y' in "Python")
# # print(87 in [95, 87, 92])
# # print("AI" in {"Python", "AI", "Beginner"})
# # print('z' in "Python")
# # print(100 in [95, 87, 92])
# # print("SQL" in {"Python", "AI", "Beginner"})


# # mixed = [42, "hello", True, 3.14, [1, 2, 3]]
# # print(len(mixed))
# # print(type(mixed[0]))
# # print(type(mixed[1]))
# # print(type(mixed[4]))

# matrix = [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]
# print(matrix[1][2])
# print(matrix[0][0])
# print(matrix[2][1])


article_tags = [
{"Python", "AI"},
{"Python", "Web"},
{"AI", "ML"},
]
print(article_tags[0])
print("AI" in article_tags[1])
print(len(article_tags))

data = [
("Alice", {95, 87, 92}),
("Bob", {78, 85, 90}),
]
print(data[0][0])
print(data[1][1])
print(88 in data[0][1])