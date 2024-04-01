class Auth:
    def __init__(self):
        self.lis={}
    def login(self,username,password):
        if username==password:
                return 1
        else:
            return 0
            # print("No user Found")
            # print("We are create a new account for u....")
    # def login(self,user_id,passwd):
    #     if(user_id not in self.lis):
    #         self.lis[user_id] = passwd
    #         return 1
    #     elif(self.lis[user_id] == passwd):
    #         return 1
    #     else:
    #         return 0
