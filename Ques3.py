#3. Write a python script to create a to print the above user account object using operator overloading (hint __str__ method).?
class UserAccount:
    def __init__(self, userid, balance):
        self.userid = userid
        self.balance = balance
        
    def __add__(self, other):
        new_userid = self.userid + other.userid
        new_balance = self.balance + other.balance
        return UserAccount(new_userid, new_balance)
    
    def __str__(self):
        return f"User:{total_user.userid} Balance:{total_user.balance}"

user1 = UserAccount(1, 100)
user2 = UserAccount(2, 200)
user3 = UserAccount(3, 300)

total_user = user1 + user2 + user3
print(total_user)
