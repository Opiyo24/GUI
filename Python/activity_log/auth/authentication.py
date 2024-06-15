import uuid
import bcrypt

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = self._hash_password(password)
        self._id = str(uuid.uuid4())
        self.is_authenticated = False
        
    def _hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password
    
    def check_password(self, password):
        return bcrypt.chcekpw(password.encode('utf-8'), self.password)
    

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