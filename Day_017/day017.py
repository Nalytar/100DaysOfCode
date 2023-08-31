# udemy Course - 100 Days of Code - Python

# Object-oriented programming custom classes

class User:
    # Constructor used to initialize the object
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User("001", "Angela")
# Creating a new variable that's attached to an object
# user_1.id = "001"
# user_1.username = "angela"
user_2 = User("002", "Jack")

user_1.follow(user_2)
print(user_1.following)
