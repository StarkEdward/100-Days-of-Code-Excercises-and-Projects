# Creating a class
class User:

    def __init__(self,user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0
    # creating method
    def follow(self, user):
        user.follower += 1
        self.following += 1

        # print("New User has been created....")


# creating a object
user_1 = User("001", "Edward") # class name start with first letter in Capital letter eg:- Sagar, Car, Game
user_2 = User("002", "Jarvis")

user_1.follow(user_2)
print("User1 Follower: ", user_1.follower)
print("User1 Following: ", user_1.following)
print("User2 Follower: ", user_2.follower)
print("User2 Following: ", user_2.following)
# print(user_1.username)

# print(user_1.id)
# print(user_1.follower)
# user_1.follow(use)


print(user_2.username)
print(user_2.id)