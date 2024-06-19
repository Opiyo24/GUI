import uuid
import bcrypt

user_authenticated = False

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = self._hash_password(password)
        self._id = str(uuid.uuid4())
        # self.is_authenticated = False
        
    def _hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password
    
    def check_password(self, password):
        return bcrypt.chcekpw(password.encode('utf-8'), self.password)
    

    # def is_authenticated(self):
    #     return self.is_authenticated
    
    @property
    def id(self):
        return self._id
    
def is_authenticated(username, widget1, password):
    global user_authenticated
    
    if username.get() == '' or password.get() == '':
        widget1.configure(text='Please fill in all fields')
        user_authenticated = False
        return False
    elif username.get() == 'Nashon' and password.get() == 'nashon':
        widget1.configure(text='Login successful')
        user_authenticated = True
        return True
    else:
        widget1.configure(text='Invalid credentials')
        user_authenticated = False
        return False