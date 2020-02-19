from mongoengine import *
from passlib.hash import pbkdf2_sha256 as sha256
from dam import db

class UserModel(Document):
    email = EmailField(max_length=254, unique=True)
    password = StringField(max_length=512, nullable=False)
    is_admin = BooleanField(default=False)
    
    def authenticate(self): return self.objects.get("email"=self.email, "password"=self.hashed(self.password))
    
    @staticmethod
    def hashed(password): return sha256.hash(password)
    