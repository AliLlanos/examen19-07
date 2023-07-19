class User:
    def __init__(self, id_user, name, age):
        self.id_user = id_user
        self.name = name
        self.age = age

class UserRepo:
    def __init__(self):
        self.users = []

    def add_user(self, id_user, name, age):
        user = User(id_user, name, age)
        self.users.append(user)
        return user

    def get_user(self, id_user):
        for user in self.users:
            if user.id_user == id_user:
                return user
        return None




