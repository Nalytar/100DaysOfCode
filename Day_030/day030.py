# udemy Course - 100 Days of Code - Python
#
# try:
# 	# Something that might cause an exception
# 	with open("afile.txt") as file:
# 		file.read()
# except FileNotFoundError:
# 	# Do this if there was an exception
# 	print("No such File exists")
# else:
# 	# Do this if there were no expections
# 	print("Thats new for me")
# finally:
# 	# Do this not matter what happens
# 	print("Lel I threw an error")
# 	raise KeyError("There is no Key-Error") throw your own Error with a Message

# Exercise Index ErrorHandling

fruits = ["apple", "pear", "orange"]


def make_pie(index):
	try:
		fruit = fruits[index]
		print(fruit + " pie")
	except IndexError:
		print("Fruit pie")


make_pie(2)

# Exercise Key ErrorHandling

facebook_posts = [{"Likes": 21},
				  {"Likes": 13, "Comments": 2, "Shares": 1},
				  {"Likes": 33, "Comments": 8, "Shares": 8},
				  {"Comments": 4, "Shares": 2},
				  {"Comments": 1, "Shares": 1},
				  {"Likes": 19, "Comments": 3}]

total_likes = 0

for post in facebook_posts:
	try:
		total_likes = total_likes + post["Likes"]
	except KeyError:
		continue


print(total_likes)
