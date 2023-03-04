#2. Write a python script to create a user account class with 2 instance variables (userid and balance). 
#   Create 3 user objects and add all the users using operator overloading.?
class UserAccount:
    def __init__(self, userid, balance):
        self.userid = userid
        self.balance = balance
        
    def __add__(self, other):
        new_userid = self.userid + other.userid
        new_balance = self.balance + other.balance
        return UserAccount(new_userid, new_balance)

user1 = UserAccount(1, 100)
user2 = UserAccount(2, 200)
user3 = UserAccount(3, 300)

total_user = user1 + user2 + user3
print(f"Total userid: {total_user.userid}")
print(f"Total balance: {total_user.balance}")
