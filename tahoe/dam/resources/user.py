import falcon
##from app.controllers.user import UserController
from dam import db
from dam.models.user_model import UserModel


class UserRegister(object):
    def on_post(self, req, resp):
        email = resp.get_json('email', dtype=str)
        password = resp.get_json('password', dtype=str)
        
        if UserModel.objects.get("email" = email):
            resp.json = {'message': 'Email {} already exists'.format(email)}, resp.status=falcon.HTTP_409
            return
        
        user_obj = UserModel(
            email = email, 
            password = UserModel.generate_hash(password),
        )
        
        try: 
            user_obj.save()
            resp.json = {'message': 'Your user has been registered'}, resp.status=falcon.HTTP_201
        except:
            resp.json = {'message': 'Something went wrong'}, resp.status=falcon.HTTP_500
            

class UserLogin(object):
    def on_post(self, req, resp):
        user = req.context['user']
        resp.body = "User Found: {}".format(user['username'])

        