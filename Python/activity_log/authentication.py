import uuid

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._id = str(uuid.uuid4())
        self.is_authenticated = False
        

    def is_authenticated(self):
        return self.is_authenticated
    
    @property
    def id(self):
        return self._id
    

# person = User('Gabriel', 'Gabriel')
# print(person.id)

# # person.is_authenticated = True

# if person.is_authenticated:
#     print("This user is authenticated")
# else:
#     print('User is NOT authenticated')